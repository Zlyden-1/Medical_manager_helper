import re

from pydantic import StringConstraints, SecretStr, BaseModel, ConfigDict


class CustomSecretStr(SecretStr, str):
    pass


class AbstractDTO(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        use_enum_values=True,
        arbitrary_types_allowed=True
    )
