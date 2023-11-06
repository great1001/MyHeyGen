import argparse
import requests
import json
from core.engine import Engine

with open('config.json', 'r') as f:
    config = json.load(f)


def translate(video_filename, output_language, output_filename):
    engine = Engine(config, output_language)
    engine(video_filename, output_filename)

if __name__ == '__main__':
    langs = ['en', 'es', 'fr', 'de', 'it', 'pt', 'pl', 'tr', 'ru', 'nl', 'cs', 'ar', 'zh-cn', 'ja']
    parser = argparse.ArgumentParser(description='Combine an audio file and a video file into a new video file')
    parser.add_argument('video_filename', help='path to video file')
    parser.add_argument('output_language', choices=list(langs), default='rus', help='choose one option')
    parser.add_argument('-o', '--output_filename', default='output.mp4', help='output file name (default: output.mp4)')
    args = parser.parse_args()

    translate(
        video_filename=args.video_filename,
        output_language=args.output_language,
        output_filename=args.output_filename,
    )