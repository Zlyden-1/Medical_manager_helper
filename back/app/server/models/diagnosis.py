from typing import List
from datetime import date

from pydantic import BaseModel, Field


class DiagnosisStandardSchema(BaseModel):
    name: str = Field(...)
    speciality: str = Field(...)
    prescriptions: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Вазомоторный ринит",
                "speciality": "Ортоларингология",
                "prescriptions": ["Флюорография легких", "Электрокардиография в покое"]
            }
        }


class RatedDiagnosisSchema(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "name": "Вазомоторный ринит",
                "speciality": "Ортоларингология",
                "prescriptions": ["Флюорография легких", "Электрокардиография в покое"],
                "extra_prescriptions": ["Креатинин"],
                "code": 2,
                "doctor_name": 'Иван Иванович',
                "protocol_name": "Ортоларингологическое отделение",
                "upload_date": date(1900, 1, 1),
            }
        }


class RatedDiagnosisResponseSchema(BaseModel):
    class Config:
        schema_extra = {
            "example": {"данные": [
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
                    "Дата загрузки": date(2000, 1, 1)
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
                    "Лишние назначения": [],
                    "Оценка":"Ок",
                    "Имя врача": 'Иван Петрович',
                    "Источник данных": "Ортоларингологическое_отделение.xlsx",
                    "Дата загрузки": date(2000, 2, 1),
                }
            ],
                "имя файла": "Ортоларингологическое_отделение.docx"
            }
        }


def single_object_response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def rated_diagnoses_response_model(data: list, filenane):
    return {
        "data": data,        "data": data,

        "code": 200,
        "filename": filenane,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
