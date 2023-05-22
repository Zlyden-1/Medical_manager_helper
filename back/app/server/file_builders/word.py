import os
from typing import List
from datetime import date

import docx


async def builder(filename: str, data: List[dict]) -> str:
    doc = docx.Document()
    table = doc.add_table(rows=1, cols=len(data[0]))
    heading_cells = table.rows[0].cells
    for i, key in enumerate(data[0].keys()):
        heading_cells[i].text = key
    for item in data:
        row_cells = table.add_row().cells
        for i, key in enumerate(item.keys()):
            row_cells[i].text = str(item[key])
    filename = find_free_filename(filename)
    doc.save(f'../media/{filename}')
    return ''


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
                    "speciality": "Ортоларингология",
                    "prescriptions": ["Флюорография легких", "Электрокардиография в покое"],
                    "extra_prescriptions": ["Креатинин"],
                    "code": 2,
                    "doctor_name": 'Иван Иванович',
                    "protocol_name": "Ортоларингологическое отделение",
                    "upload_date": date(1900, 1, 1)
                },
                {
                    "name": "Вазомоторный ринит",
                    "speciality": "Ортоларингология",
                    "prescriptions": ["Флюорография легких", "Электрокардиография в покое"],
                    "extra_prescriptions": [],
                    "code": 0,
                    "doctor_name": 'Иван Петрович',
                    "protocol_name": "Ортоларингологическое отделение",
                    "upload_date": date(1900, 2, 1),
                }
            ])))
