from fastapi import FastAPI

from server.routes.diagnosis import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Diagnoses"], prefix="/diagnoses")

