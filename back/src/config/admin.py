from typing import Dict, Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class AdminConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='admin_')

    superuser_login: str = 'admin'
    superuser_password: str = 'admin'

    secret: str = 'secret'
    session_ttl_sec: int = 10


ADMIN_CONFIG = AdminConfig()
