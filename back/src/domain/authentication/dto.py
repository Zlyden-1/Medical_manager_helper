from typing import Self, Annotated
from uuid import UUID

from src.domain.abc.dto import CustomSecretStr, AbstractDTO
from src.utils.time import get_now_with_delta


class UserSignInDTO(AbstractDTO):
    email: str
    password: CustomSecretStr


class AccessTokenDTO(AbstractDTO):
    sub: UUID
    exp: int

    @classmethod
    def factory(cls, id: UUID, exp: int) -> Self:
        return cls(
            sub=id,
            exp=int(get_now_with_delta(seconds=exp).timestamp())
        )


class RefreshTokenDTO(AbstractDTO):
    user_id: UUID

    @classmethod
    def factory(cls, refresh_token_value: str):
        return cls(
            user_id=refresh_token_value,
        )
