import re


def clean_html(text):
    return re.sub(r'<[^>]+>', '', text)
