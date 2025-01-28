from typing import Annotated

import fastapi

from src.database.redis.connection import RedisSession, API_REDIS_CONNECTION, ADMIN_REDIS_CONNECTION


def create_api_redis_session() -> RedisSession:
    return RedisSession(API_REDIS_CONNECTION)


def create_admin_redis_session() -> RedisSession:
    return RedisSession(ADMIN_REDIS_CONNECTION)


get_api_redis_session = Annotated[
    RedisSession, fastapi.Depends(create_api_redis_session)
]
