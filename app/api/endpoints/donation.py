from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models.user import User
from app.schemas.donation import DonationCreate, DonationDB, DonationFullInfoDB
from app.services.investment import invest

router = APIRouter()

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.get(
    '/',
    response_model=List[DonationFullInfoDB],
    summary='Показать список всех пожертвований',
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(session: SessionDep):
    """Только для суперпользователя."""
    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    response_model=List[DonationDB],
    summary='Показать мои пожертвования',
)
async def get_my_donations(
    session: SessionDep,
    user: User = Depends(current_user),
):
    """Для зарегистрированного пользователя — его пожертвования."""
    return await donation_crud.get_by_user(user, session)


@router.post(
    '/',
    response_model=DonationDB,
    summary='Создать пожертвование',
)
async def create_donation(
    donation_in: DonationCreate,
    session: SessionDep,
    user: User = Depends(current_user),
):
    """Для зарегистрированного пользователя."""
    new_donation = await donation_crud.create(donation_in, session)
    new_donation.user_id = user.id
    open_projects = await charity_project_crud.get_not_fully_invested(session)
    changed = invest(new_donation, open_projects)
    return await donation_crud.invest_donation(new_donation, changed, session)
