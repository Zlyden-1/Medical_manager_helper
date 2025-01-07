from typing import Iterable
from uuid import UUID

from sqlalchemy import select

from src.domain.abc.dal import AbstractDAO
from src.domain.user.dto import UserGetDTO, UserCreateDTO, UserUpdateDTO, UserSecureCredentialsDTO
from src.domain.user.model import UserModel


class UserDAO(
    AbstractDAO[
        UserModel,
        UserGetDTO,
        UserCreateDTO,
        UserUpdateDTO
    ]
):
    model = UserModel
    get_scheme = UserGetDTO
    create_scheme = UserCreateDTO
    update_scheme = UserUpdateDTO

    async def get_by_email(self, email: str) -> UserSecureCredentialsDTO | None:
        query = select(
            self.model
        ).where(
            self.model.email == email
        )
        result = await self.session.scalar(query)
        if result is None:
            return None

        return UserSecureCredentialsDTO.model_validate(result)
