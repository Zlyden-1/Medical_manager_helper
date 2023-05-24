from typing import List

from fastapi import APIRouter, Body, UploadFile, Response, File
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_rated_diagnosis,
    retrieve_rated_diagnoses,
    retrieve_diagnosis_standard_by_name,
    retrieve_diagnosis_standards,
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


@router.post("/upload/protocols", response_description="Protocols uploaded")
async def upload_protocols(name: str, file: UploadFile = File(...)) -> List[RatedDiagnosisResponseSchema]:
    result, filename = await rate_prescriptions(name, file.file)
    return rated_diagnoses_response_model(result, filename)


@router.post("/upload/standards", response_description="Standards uploaded")
async def upload_standards(file: UploadFile = File(...)):
    result = await add_standards(file.file)
    if result:
        return Response({"message": 'Standards uploaded and saved successfully'}, status_code=200)


@router.get("/download/{filename}", response_description="Report downloaded")
async def download_report(filename: str) -> FileResponse:
    return FileResponse(f'../media/{filename}', media_type='multipart/form-data')
