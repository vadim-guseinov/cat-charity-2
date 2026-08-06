from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Схема для чтения данных пользователя."""
    pass


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания пользователя."""
    pass


class UserUpdate(schemas.BaseUserUpdate):
    """Схема для обновления данных пользователя."""
    pass
