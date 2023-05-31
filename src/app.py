from os import getenv

import openai

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


if __name__ == '__main__':
    generate_text_by_question('What is the distance between the earth and mars?', 'user', 'gpt-3.5-turbo')
    generate_image_by_request('A cute yellow fish inside a fish bowl in mars', 1, '1024x1024')
