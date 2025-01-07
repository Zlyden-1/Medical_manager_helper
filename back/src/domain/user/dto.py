import enum
import datetime
from typing import Annotated
from uuid import UUID

from pydantic import SecretStr, Field

from src.domain.abc.dto import AbstractDTO


class UserCreateDTO(AbstractDTO):
    email: str
    password: SecretStr


class UserGetDTO(AbstractDTO):
    id: UUID = Field(...)
    email: str = Field(...)
    first_name: str | None = Field(None)
    surname: str | None = Field(None)
    patronymic: str | None = Field(None)


class UserUpdateDTO(AbstractDTO):
    id: UUID = Field(...)
    first_name: str | None = Field(None)
    surname: str | None = Field(None)
    patronymic: str | None = Field(None)


class UserSecureCredentialsDTO(AbstractDTO):
    id: UUID = Field(...)
    password: str = Field(...)
