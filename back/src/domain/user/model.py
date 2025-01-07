import datetime
from uuid import uuid4

from sqlalchemy import String, UUID, func, ForeignKey, BigInteger, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.abc.model import AbstractModel


class UserModel(AbstractModel):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)

    first_name: Mapped[str] = mapped_column(String(32), nullable=True)
    surname: Mapped[str] = mapped_column(String(32), nullable=True)
    patronymic: Mapped[str] = mapped_column(String(32), nullable=True)
    birthdate: Mapped[datetime.date] = mapped_column(Date, nullable=True)