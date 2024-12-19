from fastapi import FastAPI, Response, Request

from app.server.routes.diagnosis import router as StudentRouter
from fastapi.middleware.cors import CORSMiddleware
from starlette.background import BackgroundTask
from starlette.types import Message
from typing import Dict, Any
import logging


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(StudentRouter, tags=["Diagnoses"], prefix="/api/diagnoses")

logging.basicConfig(filename='info.log', level=logging.DEBUG)


def log_info(req_body, res_body):
    logging.info(req_body)
    logging.info(res_body)


# async def set_body(request: Request, body: bytes):
#     async def receive() -> Message:
#         return {'type': 'http.request', 'body': body}

#     request._receive = receive


# @app.middleware('http')
# async def some_middleware(request: Request, call_next):
#     req_body = await request.body()
#     await set_body(request, req_body)
#     response = await call_next(request)

#     res_body = b''
#     async for chunk in response.body_iterator:
#         res_body += chunk

#     task = BackgroundTask(log_info, req_body, res_body)
#     return Response(content=res_body, status_code=response.status_code,
#                     headers=dict(response.headers), media_type=response.media_type, background=task)
