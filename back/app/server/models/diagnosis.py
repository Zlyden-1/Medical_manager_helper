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
    name: str = Field(...)
    speciality: str = Field(...)
    prescriptions: List[str] = Field(...)
    extra_prescriptions: List[str] = Field(...)
    code: int = Field(...)
    doctor_name: str = Field(...)
    protocol_name: str = Field(...)
    upload_date: date = Field(...)

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
    data: List[RatedDiagnosisSchema] = Field(...)
    filename: str = Field(...)

    class Config:
        schema_extra = {
            "example": {"data": [
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
            ],
                "filename": "example.docx"
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
        "data": data,
        "code": 200,
        "filename": filenane,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
