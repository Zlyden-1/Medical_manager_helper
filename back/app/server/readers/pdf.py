import string
import re
from typing import List

from PyPDF2 import PdfReader


async def reader(filename) -> List[str]:
    reader_ = PdfReader(f"../media/{filename}")
    parts = []
    # TODO: вынимать еще и возраст!!!!!!!!!!!!!!!!!

    def visitor_body(text: str, cm, tm, fontDict, fontSize):
        if len(text) > 1:
            text = text.strip()
        parts.append(text)

    for page in reader_.pages:
        page.extract_text(visitor_text=visitor_body)
    parts = [i for i in parts if i and (i[0].isalpha() or (i[0] in string.punctuation))]
    lab_methods_1 = parts[parts.index('Лабораторные методы исследования') + 13: parts.index('Инструментальные методы')]
    instrumental_methods_1 = parts[parts.index('Инструментальные методы') + 14: parts.index('Инструментальные методы')]
    parts = lab_methods_1 + instrumental_methods_1
    text_body = "\n".join(parts)
    parts = re.split(r'[A-ZА-Я]\d\d.[\d.]+', text_body)
    prescriptions = [' '.join([_ for _ in i.split('\n') if _]) for i in parts]
    return prescriptions


if __name__ == '__main__':
    print(reader('Приказ_М.pdf'))


