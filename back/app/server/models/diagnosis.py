from typing import Optional, List

from pydantic import BaseModel, Field


class DiagnosisSchema(BaseModel):
    name: str = Field(...)
    speciality: str = Field(...)
    prescriptions: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Вазомоторный ринит",
                "prescriptions": ["Флюорография легких", "Электрокардиография в покое"]
            }
        }


class RatedDiagnosisSchema(BaseModel):
    name: str = Field(...)
    speciality: str = Field(...)
    prescriptions: List[str] = Field(...)
    extra_prescriptions: List[str] = Field(...)
    code: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Вазомоторный ринит",
                "speciality": "Ортоларингология",
                "prescriptions": ["Флюорография легких", "Электрокардиография в покое"],
                "extra_prescriptions": ["Креатинин"],
                "code": 2,
            }
        }


class UpdateStudentModel(BaseModel):
    name: Optional[str] = Field(...)
    prescriptions: Optional[List[str]] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Вазомоторный ринит",
                "prescriptions": ["Флюорография легких", "Электрокардиография в покое"]
            }
        }


def single_object_response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def multi_object_response_model(data: list, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
