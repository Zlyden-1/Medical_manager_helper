from src.api.rest.v1.auth.exception import ConflictPhone
from src.database.postgres.depends import get_session
from src.domain.authentication.service import Hasher
from src.domain.user.dal import UserDAO
from src.domain.user.dto import UserCreateDTO, UserGetDTO


async def user_create(session: get_session, user_data: UserCreateDTO) -> UserGetDTO:
    conflict_by_email_user = await UserDAO(session).get_by_email(user_data.email)
    if conflict_by_email_user is not None:
        raise ConflictPhone

    user_data.password = Hasher.get_password_hash(user_data.password)
    data_to_insert = UserCreateDTO.model_validate(user_data)
    new_user = await UserDAO(session).create(data_to_insert)
    return new_user
