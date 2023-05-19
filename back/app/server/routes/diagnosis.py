from typing import List

from fastapi import APIRouter, Body, UploadFile
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_diagnosis,
    delete_diagnosis,
    retrieve_diagnoses,
    retrieve_diagnosis_by_name,
    update_diagnosis,
)
from ..models.diagnosis import (
    error_response_model,
    single_object_response_model,
    multi_object_response_model,
    DiagnosisSchema,
    RatedDiagnosisSchema,
    UpdateStudentModel,
)
from ..readers.xslx import xslx_reader
from ..controllers.diagnosis import rate_prescriptions

router = APIRouter()


# @router.post("/", response_description="Student data added into the database")
# async def add_student_data(diagnosis: DiagnosisSchema = Body(...)):
#     diagnosis = jsonable_encoder(diagnosis)
#     new_diagnosis = await add_student(diagnosis)
#     return response_model(new_student, "Student added successfully.")

#
# @router.get("/", response_description="Diagnoses retrieved")
# async def get_students():
#     diagnoses = await retrieve_diagnoses()
#     if diagnoses:
#         return multi_object_response_model(diagnoses, "Diagnoses data retrieved successfully")
#     return multi_object_response_model(diagnoses, "Empty list returned")
#
#
# @router.get("/{id}", response_description="Diagnosis data retrieved")
# async def get_student_data(id):
#     student = await single_object_response_model(id)
#     if student:
#         return single_object_response_model(student, "Diagnosis data retrieved successfully")
#     return error_response_model("An error occurred.", 404, "Diagnosis doesn't exist.")

@router.post("/", response_description="Protocols uploaded")
async def upload_protocols(file: UploadFile) -> List[RatedDiagnosisSchema]:
    data: list[dict] = await xslx_reader(file.file)
    result = await rate_prescriptions(data)
    return multi_object_response_model(result, 'Protocols uploaded and rated successfully')
