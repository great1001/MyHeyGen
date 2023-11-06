from TTS.api import TTS
from core.temp_manager import TempFileManager

class VoiceCloner:
    def __init__(self, lang_code):
        # self.api = TTS(f'tts_models/{lang_code}/fairseq/vits')
        self.api = TTS(f'tts_models/multilingual/multi-dataset/xtts_v1.1')
        self.lang_code = lang_code
    
    def process(self, speaker_wav_filename, text, out_filename=None):
        temp_manager = TempFileManager()
        if not out_filename:
            out_filename = temp_manager.create_temp_file(suffix='.wav').name
        self.api.tts_to_file(
            text,
            speaker_wav=speaker_wav_filename,
            file_path=out_filename,
            language=self.lang_code
        )
        return out_filename

import re
import os
import time
import torch
import torchaudio
from tqdm import tqdm
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

class Pre_VoiceCloner:
    def __init__(self, lang_code):
        print("Loading model tts_models--multilingual--multi-dataset--xtts_v1.1")
        config = XttsConfig()
        config.load_json("/root/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v1.1/config.json")
        model = Xtts.init_from_config(config)
        model.load_checkpoint(config, checkpoint_dir="/root/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v1.1")
        model.cuda()
        self.model = model
        self.lang_code = lang_code
    
    def process(self, speaker_wav_filename, text, out_filename=None):
        temp_manager = TempFileManager()
        if not out_filename:
            out_filename = temp_manager.create_temp_file(suffix='.wav').name
        
        print("Computing speaker latents...")
        gpt_cond_latent, _, speaker_embedding = self.model.get_conditioning_latents(audio_path=speaker_wav_filename)

        print("Inference...")
        # 去除中文中的英文字符,不然 voice cloner 报错
        if 'zh' in self.lang_code:
            text = re.sub('[a-zA-Z]','', text)
            
        t0 = time.time()
        chunks = self.model.inference_stream(
            text,
            self.lang_code,
            gpt_cond_latent,
            speaker_embedding
        )

        wav_chuncks = []
        for i, chunk in enumerate(chunks):
            if i == 0:
                print(f"Time to first chunck: {time.time() - t0}")
            print(f"Received chunk {i} of audio length {chunk.shape[-1]}")
            wav_chuncks.append(chunk)
        wav = torch.cat(wav_chuncks, dim=0)
        torchaudio.save(out_filename, wav.squeeze().unsqueeze(0).cpu(), 24000,bits_per_sample=16)
        return out_filename