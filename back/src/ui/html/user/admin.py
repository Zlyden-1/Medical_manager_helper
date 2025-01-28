from sqladmin import ModelView

from src.domain.authentication.service import Hasher
from src.domain.user.model import UserModel


class UserAdmin(ModelView, model=UserModel):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"

    form_create_rules = [
        "email",
        "first_name",
        "surname",
        "patronymic",
        "birthdate",
        "password",
    ]
    form_edit_rules = [
        "email",
        "first_name",
        "surname",
        "patronymic",
        "birthdate",
    ]

    column_list = [
        UserModel.id,
        UserModel.email,
        UserModel.first_name,
        UserModel.surname,
        UserModel.patronymic,
        UserModel.birthdate,
    ]

    async def on_model_change(self, data, model, is_created, request) -> None:
        if is_created:
            data['password'] = Hasher.get_password_hash(data['password'])
