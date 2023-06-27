from typing import List
from datetime import date
import os

from fastapi import APIRouter, Body, UploadFile, Response, File
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_diagnosis_standard,
    add_rated_diagnosis,
    retrieve_rated_diagnoses,
    retrieve_diagnosis_standard_by_id,
    retrieve_diagnosis_standards, delete_diagnosis_standard,
)
from ..models.diagnosis import (
    error_response_model,
    single_object_response_model,
    rated_diagnoses_response_model,
    DiagnosisStandardSchema,
    RatedDiagnosisResponseSchema,
)
from ..readers import xslx, pdf
from ..controllers.diagnosis import rate_prescriptions, add_standards

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_diagnosis_new_standard(name: str = Body(embed=True),
                                     speciality: str = Body(embed=True),
                                     prescriptions: str = Body(embed=True),
                                     extra_prescriptions: List = Body(embed=True)):

    diagnosis = {'Диагноз': name,
                 'Направление': speciality,
                 'Возраст': prescriptions,
                 'Назначения': extra_prescriptions,
                 }
    new_diagnosis = await add_diagnosis_standard(diagnosis)
    return new_diagnosis


#
# @router.get("/", response_description="Diagnoses retrieved")
# async def get_rated_diagnoses():
#     diagnoses = await retrieve_rated_diagnoses()
#     if diagnoses:
#         return multi_object_response_model(diagnoses, "Diagnoses data retrieved successfully")
#     return multi_object_response_model(diagnoses, "Empty list returned")


# @router.get("/{id}", response_description="Diagnosis data retrieved")
# async def get_student_data(id):
#     student = await single_object_response_model(id)
#     if student:
#         return single_object_response_model(student, "Diagnosis data retrieved successfully")
#     return error_response_model("An error occurred.", 404, "Diagnosis doesn't exist.")


@router.post("/upload/protocols", response_description="Protocols uploaded", )
async def upload_protocols(name: str = Body(embed=True), file: UploadFile = File(...)):
    # -> List[RatedDiagnosisResponseSchema]:
    # result, filename = await rate_prescriptions(name, file.file)
    # result = sorted(result, key=lambda a: a["Дата оказания услуги"])
    # return rated_diagnoses_response_model(result, filename)
    #
    result = [
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2000, 1, 1),
            'ID пациента': 3,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Вазомоторный ринит",
            'Дата оказания услуги': date(2000, 1, 1),
            'Должность': 'врач-оториноларинголог',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": ["Креатинин"],
            "Оценка": "Избыточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1)
        },
        {
            'Пол пациента': 'Жен',
            'Дата рождения пациента': date(2002, 2, 1),
            'ID пациента': 65,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Cvthnm",
            'Дата оказания услуги': date(2002, 1, 10),
            'Должность': 'врач-травматолог',
            "Назначения": [],
            "Лишние назначения": [],
            "Оценка": "Недостаточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2005, 1, 1),
            'ID пациента': 13,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Выгорание",
            'Дата оказания услуги': date(2010, 2, 1),
            'Должность': 'врач',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое", 'Анализ кала'],
            "Лишние назначения": ['Анализ кала'],
            "Оценка": "Избыточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2012, 1, 1),
            'ID пациента': 666,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Депрессия",
            'Дата оказания услуги': date(2020, 1, 1),
            'Должность': 'врач-психиатр',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": [],
            "Оценка": "Ок",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2000, 1, 1),
            'ID пациента': 444,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Вазомоторный ринит",
            'Дата оказания услуги': date(2020, 12, 1),
            'Должность': 'врач-оториноларинголог',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": [],
            "Оценка": "Ок",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2000, 1, 1),
            'ID пациента': 3,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Вазомоторный ринит",
            'Дата оказания услуги': date(2000, 1, 1),
            'Должность': 'врач-оториноларинголог',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": ["Креатинин"],
            "Оценка": "Избыточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1)
        },
        {
            'Пол пациента': 'Жен',
            'Дата рождения пациента': date(2002, 2, 1),
            'ID пациента': 65,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Cvthnm",
            'Дата оказания услуги': date(2002, 1, 10),
            'Должность': 'врач-травматолог',
            "Назначения": [],
            "Лишние назначения": [],
            "Оценка": "Недостаточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2005, 1, 1),
            'ID пациента': 13,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Выгорание",
            'Дата оказания услуги': date(2010, 2, 1),
            'Должность': 'врач',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое", 'Анализ кала'],
            "Лишние назначения": ['Анализ кала'],
            "Оценка": "Избыточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2012, 1, 1),
            'ID пациента': 666,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Депрессия",
            'Дата оказания услуги': date(2020, 1, 1),
            'Должность': 'врач-психиатр',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": [],
            "Оценка": "Ок",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2000, 1, 1),
            'ID пациента': 444,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Вазомоторный ринит",
            'Дата оказания услуги': date(2020, 12, 1),
            'Должность': 'врач-оториноларинголог',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": [],
            "Оценка": "Ок",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2000, 1, 1),
            'ID пациента': 3,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Вазомоторный ринит",
            'Дата оказания услуги': date(2000, 1, 1),
            'Должность': 'врач-оториноларинголог',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": ["Креатинин"],
            "Оценка": "Избыточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1)
        },
        {
            'Пол пациента': 'Жен',
            'Дата рождения пациента': date(2002, 2, 1),
            'ID пациента': 65,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Cvthnm",
            'Дата оказания услуги': date(2002, 1, 10),
            'Должность': 'врач-травматолог',
            "Назначения": [],
            "Лишние назначения": [],
            "Оценка": "Недостаточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2005, 1, 1),
            'ID пациента': 13,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Выгорание",
            'Дата оказания услуги': date(2010, 2, 1),
            'Должность': 'врач',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое", 'Анализ кала'],
            "Лишние назначения": ['Анализ кала'],
            "Оценка": "Избыточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2012, 1, 1),
            'ID пациента': 666,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Депрессия",
            'Дата оказания услуги': date(2020, 1, 1),
            'Должность': 'врач-психиатр',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": [],
            "Оценка": "Ок",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2000, 1, 1),
            'ID пациента': 444,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Вазомоторный ринит",
            'Дата оказания услуги': date(2020, 12, 1),
            'Должность': 'врач-оториноларинголог',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое"],
            "Лишние назначения": [],
            "Оценка": "Ок",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
    ]
    filename = 'test_1.docx'
    result = sorted(result, key=lambda a: a["Дата оказания услуги"])
    return rated_diagnoses_response_model(result, filename)


@router.get("/download/{filename}", response_description="Report downloaded")
async def download_report(filename: str) -> FileResponse:
    return FileResponse(
        os.path.abspath(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/media/{filename}'),
        media_type='multipart/form-data')


@router.post("/upload/standards", response_description="Standards uploaded")
async def upload_standards(name: str = Body(embed=True), speciality: str = Body(embed=True),
                           file: UploadFile = File(...)):
    result = await add_standards(name, speciality, file)
    if result:
        return result


@router.get("/standards", response_description="Standards retrieved")
async def get_standards():
    result = await retrieve_diagnosis_standards()
    if result:
        return result
    else:
        return Response('Нет данных о стандартах', status_code=404)


@router.delete("/standards/delete/{id}", response_description="Standard deleted")
async def delete_standard(id):
    result = await delete_diagnosis_standard(id=id)
    return Response({"данные": result}, status_code=200)


if __name__ == '__main__':
    print(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/media/test_1.docx')
