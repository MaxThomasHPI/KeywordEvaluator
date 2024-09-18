import os


def get_introduction_text():
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, '..', '..', 'static/text_content/introduction_text.txt')

    with open(path, 'r') as f:
        introduction_text = f.read()

    return introduction_text
