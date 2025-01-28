from sqladmin import ModelView
from src.domain.user.model import UserModel


class UserAdmin(ModelView, model=UserModel):
    column_list = [
        UserModel.id,
        UserModel.email,
        UserModel.first_name,
        UserModel.surname,
        UserModel.patronymic,
        UserModel.birthdate,
    ]