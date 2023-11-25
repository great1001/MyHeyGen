#米海根
一个平民版视频翻译工具，音频翻译，翻译校正，视频唇纹合成全流程解决方案
## 参考项目（感谢他们的优秀作品）
[海根克隆](https://github.com/BrasD99/HeyGenClone.git)、[自文本至语音的转换](https://github.com/coqui-ai/tts)、[视频回放](https://github.com/OpenTalker/video-retalking)
## 实现效果
- [【艾小美的英语,汉语,法语,俄语本当上手】](https://www.bilibili.com/video/BV1YQ4y1n7Ym/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)
- [【海根或十一实验室会员太贵了,原来可以白嫖方案的！】](https://www.bilibili.com/video/BV17c411d7LK/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)
- [【张三老师英文普法！英文区的网友有福啦】](https://www.bilibili.com/video/BV1XN41137Bv/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)
## 视频教程
[【MyHeyGen来了！！！】]( https://www.bilibili.com/video/BV14C4y1J7dY/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)

## 环境准备
1. 在[拥抱脸申请代币](https://huggingface.co/),放在config.json的HF_TOKEN参数下
2. 在[百度翻译申请APPKey](https://fanyi-api.baidu.com/?fr=pcHeader)用于翻译字幕放在config.json的TS_APPID和TS_APPKEY参数下
3. 下载[砝码](https://drive.google.com/file/d/1dYy24q_58TmVuv_PbChe2t1zpNYJci1J/view?usp=sharing)放在MyHeyGen目录下，下载[检查站](https://drive.google.com/drive/folders/18rhjMpxK8LVVxf7PI6XwOidt7Vouv_H0?usp=share_link)放在video-retalking目录下,从weights复制GFPGANv1.4.pth到checkpoints
4.仅在Linux python 3.10特斯拉T4(16GB)环境下测试通过

## 安装
```
饭桶克隆https://github.com/AIFSH/MyHeyGen.git
cd MyHeyGen
bash install.sh
```
## 测试
```
大蟒翻译py/root/MyHeyGen/test/src。MP4 ' zh-cn '-o/root/MyHeyGen/test/out _ zh。MP4
```
## 自己使用
```
python translate.py 原视频文件路径 想要翻译成的语言代码 -o 翻译好的视频路径
## 语言代码可以选择这些中之一：['en', 'es', 'fr', 'de', 'it', 'pt', 'pl', 'tr', 'ru', 'nl', 'cs', 'ar', 'zh-cn', 'ja']
##分别对应[英语、西班牙语、法语、德语、意大利语、葡萄牙语、波兰语、土耳其语、俄语、荷兰语、捷克语、阿拉伯语、中文（简体）、日语]14种语言
```
