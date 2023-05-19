import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://mongodb:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.diagnosis

diagnosis_collection = database.get_collection("diagnosis_collection")


def diagnosis_helper(diagnosis) -> dict:
    return {
        "id": str(diagnosis["_id"]),
        "name": diagnosis["name"],
        "speciality": diagnosis["speciality"],
        "prescriptions": diagnosis["prescriptions"],
    }


# Retrieve all students present in the database
async def retrieve_diagnoses():
    diagnoses = []
    async for diagnosis in diagnosis_collection.find():
        diagnoses.append(diagnosis_helper(diagnosis))
    return diagnoses


# Add a new student into to the database
async def add_diagnosis(diagnosis_data: dict) -> dict:
    diagnosis = await diagnosis_collection.insert_one(diagnosis_data)
    new_student = await diagnosis_collection.find_one({"_id": diagnosis.inserted_id})
    return diagnosis_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_diagnosis_by_name(name: str) -> dict:
    diagnosis = await diagnosis_collection.find_one({"name": name})
    if diagnosis:
        return diagnosis_helper(diagnosis)


# Update a student with a matching ID
async def update_diagnosis(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await diagnosis_collection.find_one({"_id": ObjectId(id)})
    if student:
        diagnosis_student = await diagnosis_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if diagnosis_student:
            return True
        return False


# Delete a student from the database
async def delete_diagnosis(id: str):
    student = await diagnosis_collection.find_one({"_id": ObjectId(id)})
    if student:
        await diagnosis_collection.delete_one({"_id": ObjectId(id)})
        return True
