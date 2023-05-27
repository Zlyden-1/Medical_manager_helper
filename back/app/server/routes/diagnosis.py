from typing import List
from datetime import date

from fastapi import APIRouter, Body, UploadFile, Response, File
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_rated_diagnosis,
    retrieve_rated_diagnoses,
    retrieve_diagnosis_standard_by_name,
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


# @router.post("/", response_description="Student data added into the database")
# async def add_student_data(diagnosis: DiagnosisStandardSchema = Body(...)):
#     diagnosis = jsonable_encoder(diagnosis)
#     new_diagnosis = await add_student(diagnosis)
#     return response_model(new_student, "Student added successfully.")

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
    # result = sorted(result, key=lambda a: a["Дата оказания услуги"]
    # return rated_diagnoses_response_model(result, filename)
    return {"данные": [
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
            "Диагноз": "Отвал жопы",
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
            "Диагноз": "Разрыв очка",
            'Дата оказания услуги': date(2010, 2, 1),
            'Должность': 'врач-пидарас',
            "Назначения": ["Флюорография легких", "Электрокардиография в покое", 'Минет'],
            "Лишние назначения": ['Минет'],
            "Оценка": "Избыточные назначения",
            "Источник данных": "Ортоларингологическое_отделение.xlsx",
            "Дата загрузки": date(2000, 2, 1),
        },
        {
            'Пол пациента': 'Муж',
            'Дата рождения пациента': date(2012, 1, 1),
            'ID пациента': 666,
            'Код МКБ-10': 'J32.9',
            "Диагноз": "Хуй Васильевича",
            'Дата оказания услуги': date(2020, 1, 1),
            'Должность': 'врач-блять что это',
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
    ],
        "имя файла": "Ортоларингологическое_отделение.docx"
    }


@router.get("/download/{filename}", response_description="Report downloaded")
async def download_report(filename: str) -> FileResponse:
    return FileResponse(f'../media/{filename}', media_type='multipart/form-data')


@router.post("/upload/standards", response_description="Standards uploaded")
async def upload_standards(name: str = Body(embed=True), speciality: str = Body(embed=True),
                           file: UploadFile = File(...)):
    result = await add_standards(name, speciality, file)
    if result:
        return Response({"данные": result}, status_code=200)


@router.get("/standards", response_description="Standards retrieved")
async def get_standards():
    result = await retrieve_diagnosis_standards()
    if result:
        return Response({"данные": result}, status_code=200)


@router.get("/standards/delete/{id}", response_description="Standard deleted")
async def delete_standard(id):
    result = await delete_diagnosis_standard(id=id)
    if result:
        return Response({"данные": result}, status_code=200)

