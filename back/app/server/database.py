import asyncio

import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://127.0.0.1:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.diagnosis

rated_diagnosis_collection = database.get_collection("rated_diagnosis_collection")

diagnosis_standard_collection = database.get_collection("diagnosis_standard_collection")


def diagnosis_standard_helper(diagnosis) -> dict:
    return {
        "id": str(diagnosis["_id"]),
        "Диагноз": diagnosis["Диагноз"],
        "Направление": diagnosis["Направление"],
        "Назначения": diagnosis["Назначения"],
    }


def rated_diagnosis_helper(diagnosis) -> dict:
    return {
        "id": str(diagnosis["_id"]),
        "name": diagnosis["name"],
        "speciality": diagnosis["speciality"],
        "prescriptions": diagnosis["prescriptions"],
        "extra_prescriptions": diagnosis["extra_prescriptions"],
        "code": diagnosis["code"],
        "doctor_name": diagnosis["doctor_name"],
        "protocol_name": diagnosis["protocol_name"],
        "upload_date": diagnosis["upload_date"],
    }


# Retrieve all students present in the database
async def retrieve_rated_diagnoses():
    diagnoses = []
    async for diagnosis in rated_diagnosis_collection.find():
        diagnoses.append(rated_diagnosis_helper(diagnosis))
    return diagnoses


async def retrieve_diagnosis_standards():
    diagnoses = []
    async for diagnosis in diagnosis_standard_collection.find():
        diagnoses.append(diagnosis_standard_helper(diagnosis))
    return diagnoses


# Add a new student into to the database
async def add_rated_diagnosis(diagnosis_data: dict) -> dict:
    diagnosis = await rated_diagnosis_collection.insert_one(diagnosis_data)
    new_diagnosis = await rated_diagnosis_collection.find_one({"_id": diagnosis.inserted_id})
    return rated_diagnosis_helper(new_diagnosis)


async def add_diagnosis_standard(diagnosis_data: dict) -> dict:
    diagnosis = await diagnosis_standard_collection.insert_one(diagnosis_data)
    new_diagnosis = await diagnosis_standard_collection.find_one({"_id": diagnosis.inserted_id})
    return diagnosis_standard_helper(new_diagnosis)


async def retrieve_diagnosis_standard_by_id(id: str) -> dict:
    diagnosis = await diagnosis_standard_collection.find_one({"_id": ObjectId(id)})
    if diagnosis:
        return diagnosis_standard_helper(diagnosis)

# Update a student with a matching ID
# async def update_diagnosis(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     student = await rated_diagnosis_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         diagnosis_student = await rated_diagnosis_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if diagnosis_student:
#             return True
#         return False


async def delete_diagnosis_standard(id: str):
    diagnosis = await diagnosis_standard_collection.find_one({"_id": ObjectId(id)})
    if diagnosis:
        await diagnosis_standard_collection.delete_one({"_id": ObjectId(id)})
        return True


if __name__ == '__main__':
    # asyncio.run(add_diagnosis_standard({
    #     "Диагноз": "Перенесенный в прошлом инфаркт миокарда",
    #     "Направление": "Кардиология",
    #     "Назначения": ["Эхокардиография", "Креатинин"]
    # }))
    # asyncio.run(delete_diagnosis('646e3212f676d426cbf608f3'))
    print(asyncio.run(retrieve_diagnosis_standards()))
