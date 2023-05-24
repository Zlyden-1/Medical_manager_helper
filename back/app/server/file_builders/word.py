import os
from typing import List
from datetime import date
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.shared import Inches

import docx


async def builder(filename: str, data: List[dict]) -> str:
    doc = docx.Document()

    doc.sections[0].orientation = WD_ORIENT.LANDSCAPE
    doc.sections[0].page_width = Inches(11.69)
    doc.sections[0].page_height = Inches(8.27)

    table = doc.add_table(rows=1, cols=len(data[0]), )
    heading_cells = table.rows[0].cells
    for i, key in enumerate(data[0].keys()):
        if key != 'code':
            heading_cells[i].text = key
    for item in data:
        row_cells = table.add_row().cells
        for i, key in enumerate(item.keys()):
            if key != 'code':
                row_cells[i].text = str(item[key])
    filename = find_free_filename(filename)
    doc.save(f'../media/{filename}')
    return f'{filename}'


def find_free_filename(base_filename: str):
    filename = f'{base_filename}.docx'
    i = 1
    while os.path.exists(f'../media/{filename}'):
        filename = f"{base_filename}_{i}.docx"
        i += 1
    return filename


if __name__ == '__main__':
    import asyncio

    print(asyncio.run(builder('test', [
                {
                    "name": "Вазомоторный ринит",
                    "speciality": "Отоларингология",
                    "prescriptions": ["Флюорография легких", "Электрокардиография в покое"],
                    "extra_prescriptions": ["Креатинин"],
                    "code": 2,
                    "doctor_name": 'Иван Иванович',
                    "protocol_name": "Отоларингологическое отделение",
                    "upload_date": date(1900, 1, 1)
                },
                {
                    "name": "Вазомоторный ринит",
                    "speciality": "Отоларингология",
                    "prescriptions": ["Флюорография легких", "Электрокардиография в покое"],
                    "extra_prescriptions": [],
                    "code": 0,
                    "doctor_name": 'Иван Петрович',
                    "protocol_name": "Отоларингологическое отделение",
                    "upload_date": date(1900, 2, 1),
                }
            ])))
