from os import getenv
from os.path import join

import openai

from src import FILES_PATH

openai.api_key = getenv('OPENAI_KEY')


def generate_text_by_question(msg: str, role: str, model: str):
    result = openai.ChatCompletion.create(
        model=model,
        messages=[{'role': role, 'content': msg}]
    )

    print(result)


def generate_image_by_request(request: str, qtd: int, size: str):
    image = openai.Image.create(
        prompt=request,
        n=qtd,
        size=size
    )

    print(image)


def transcription_by_audio(audio: str):
    audio_file = open(audio, "rb")
    result = openai.Audio.translate("whisper-1", audio_file)

    print(result)


if __name__ == '__main__':
    generate_text_by_question('What is the distance between the earth and mars?', 'user', 'gpt-3.5-turbo')
    generate_image_by_request('A cute yellow fish inside a fish bowl in mars', 1, '1024x1024')
    transcription_by_audio(join(FILES_PATH, 'german1.mp3'))
