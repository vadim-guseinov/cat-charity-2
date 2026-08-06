from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class DonationCreate(BaseModel):
    """Схема для создания пожертвования."""

    full_amount: PositiveInt
    comment: Optional[str] = None

    model_config = {'extra': 'forbid'}


class DonationDB(DonationCreate):
    """Схема ответа при создании пожертвования (для владельца)."""

    id: int
    create_date: datetime

    model_config = {'from_attributes': True, 'extra': 'forbid'}


class DonationFullInfoDB(DonationCreate):
    """Схема ответа с полными данными пожертвования (для суперпользователя)."""

    id: int
    user_id: Optional[int] = None
    create_date: datetime
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime] = None

    model_config = {'from_attributes': True, 'extra': 'forbid'}
