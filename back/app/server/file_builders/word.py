import copy
import os
from typing import List
from datetime import date
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.shared import Inches
from docx.shared import RGBColor
from googletrans import Translator
from docx.shared import Cm

import docx
import pandas as pd


def translate_table_columns(table):
    """
    Переводит названия столбцов таблицы с английского на русский язык.
    :param table: таблица (Table object)
    """
    translation_dict = {"name": "Диагноз",
                        "speciality": "Специальность",
                        "prescriptions": "Назначения",
                        "doctor_name": "Имя доктора",
                        "protocol_name": "Отделение",
                        "upload_date": "Дата загрузки"}

    # перевод названий столбцов
    for col_idx, cell in enumerate(table.rows[0].cells):
        original_text = cell.text
        if original_text in translation_dict:
            cell.text = translation_dict[original_text]
    # return table


async def builder(filename: str, data: List[dict]) -> str:
    doc = docx.Document()

    doc.sections[0].orientation = WD_ORIENT.LANDSCAPE
    doc.sections[0].page_width = Inches(11.69)
    doc.sections[0].page_height = Inches(8.27)

    table = doc.add_table(rows=1, cols=len(data[0]), )
    heading_cells = table.rows[0].cells
    table.style = 'Table Grid'
    for column in table.columns:
        column.width = Inches(2)

    for i, key in enumerate(data[0].keys()):
        if key != 'code' and key != 'extra_prescriptions':
            heading_cells[i].text = key
            heading_cells[i].paragraphs[0].alignment = 1
    for item in data:
        row_cells = table.add_row().cells
        for i, key in enumerate(item.keys()):
            if item["code"] == 2:
                if key != 'code' and key != 'extra_prescriptions':
                    if type(item[key]) == list:
                        row_cells[i].text = '\n'.join(item[key])
                        row_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 0, 0)
                    else:
                        row_cells[i].text = str(item[key])
                        row_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 0, 0)
                elif key == 'extra_prescriptions':
                    cell = table.cell(1, 2)
                    nested_table = cell.add_table(rows=1, cols=1)
                    nested_cell = nested_table.cell(0, 0)
                    nested_cell.text = '\n'.join(item[key])
                    nested_cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 0, 0)
                    nested_cell.paragraphs[0].runs[0].bold = True
                else:
                    ...
            else:
                if key != 'code':
                    if type(item[key]) == list:
                        row_cells[i].text = '\n'.join(item[key])
                    else:
                        row_cells[i].text = str(item[key])

    # удаляем ячейки в четвертом и пятом столбцах
    for row in table.rows:
        row.cells[3]._element.clear()  # четвертый столбец
        row.cells[4]._element.clear()  # пятый столбец

    # удаляем четвертый и пятый столбцы
    for row in table.rows:
        row._element.remove(row._element.tc_lst[3])  # четвертый столбец
        row._element.remove(row._element.tc_lst[3])  # пятый столбец

    # переводим названия столбцов для каждой таблицы в документе
    for table in doc.tables:
        translate_table_columns(table)

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
