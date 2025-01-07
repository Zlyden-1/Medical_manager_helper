from uuid import UUID, uuid4

from src.config.auth import AUTH_CONFIG
from src.database.redis.connection import RedisSession
from src.domain.authentication.dto import RefreshTokenDTO
from src.domain.authentication.exception import RefreshNotFound


class AuthenticationDAO:
    def __init__(self, redis_session: RedisSession):
        self.redis_session = redis_session

    async def create_refresh_token(
        self,
        user_id: str | UUID
    ) -> str:
        refresh_token = str(uuid4())
        await self.redis_session.set_item(
            refresh_token,
            str(user_id),
            AUTH_CONFIG.refresh_exp_sec,
        )
        return refresh_token

    async def pop_refresh_token(
        self,
        refresh_token: str | UUID | None = None
    ) -> RefreshTokenDTO | None:
        if refresh_token is None:
            raise RefreshNotFound
        user_id = await self.redis_session.get_value(refresh_token)
        if user_id is None:
            return None

        await self.redis_session.delete_item(refresh_token)
        return RefreshTokenDTO.factory(user_id)
