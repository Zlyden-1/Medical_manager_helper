import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from src.api.rest.v1 import auth_rest_v1
from src.config.admin import ADMIN_CONFIG
from src.config.app import APP_CONFIG
from src.database.postgres.connection import engine
from src.ui.html.auth.admin import AdminAuth
from src.ui.html.user.admin import UserAdmin
from src.utils.router import include_routers


@asynccontextmanager
async def lifespan(app_: FastAPI):
    os.system('alembic upgrade head')

    v1_routers = [
        auth_rest_v1
    ]

    v1_router = include_routers(APIRouter(prefix='/v1'), v1_routers)
    main_router = include_routers(APIRouter(prefix='/api'), (v1_router,))
    app_.include_router(main_router)

    admin_auth_backend = AdminAuth(secret_key=ADMIN_CONFIG.secret)
    admin = Admin(app, engine, authentication_backend=admin_auth_backend)
    admin.add_view(UserAdmin)

    yield


app = FastAPI(debug=APP_CONFIG.debug, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['OPTIONS', 'POST', 'GET', 'DELETE'],
    allow_headers=['*'],
    allow_credentials=True
)
