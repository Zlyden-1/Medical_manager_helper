from uuid import uuid4

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.config.admin import ADMIN_CONFIG
from src.database.redis.depends import create_admin_redis_session


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        if not (username, password) == (ADMIN_CONFIG.superuser_login, ADMIN_CONFIG.superuser_password):
            return False
        redis_session = create_admin_redis_session()
        session_token = str(uuid4())
        await redis_session.set_item(session_token, ADMIN_CONFIG.superuser_login, ADMIN_CONFIG.session_ttl_sec)
        request.session.update({"token": session_token})

        return True

    async def logout(self, request: Request) -> bool:
        redis_session = create_admin_redis_session()

        if token := request.session.get("token"):
            await redis_session.delete_item(token)

        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        redis_session = create_admin_redis_session()
        user = await redis_session.get_value(token)

        if user != ADMIN_CONFIG.superuser_login:
            return False

        return True
