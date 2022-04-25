import typing as t

import hikari
from attr import fields
from attrs import asdict, filters
from fastapi import (
    APIRouter,
    Depends,
    status,
    Response,
    Request
)
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import RedirectResponse, JSONResponse

from backend.services import (
    AuthService,
    UserService
)


router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@router.post("/")
async def get_user(token=Depends(AuthService.requires_authorization)):
    user = await UserService.fetch_user(token)
    return asdict(user, filter=filters.exclude(fields(hikari.OwnUser).app))


@router.post(
    "/guilds",
    dependencies=[Depends(AuthService.requires_authorization)],
)
async def get_guilds(token=Depends(AuthService.requires_authorization)):
    return [asdict(guild, filter=filters.exclude(fields(hikari.OwnGuild).app))
            for guild in await UserService.fetch_guilds(token)]


@router.post(
    "/guilds/hasperms",
    dependencies=[Depends(AuthService.requires_authorization)],
)
async def get_guilds_hasperms(token=Depends(AuthService.requires_authorization)):
    return [asdict(guild, filter=filters.exclude(fields(hikari.OwnGuild).app))
            for guild in await UserService.fetch_guilds_with_manage_server_perm(token)]


@router.post(
    "/guilds/hasperms/mutual",
    dependencies=[Depends(AuthService.requires_authorization)],
)
async def get_guilds_hasperms_mutual(token=Depends(AuthService.requires_authorization)):
    guilds = await UserService.fetch_guilds_with_manage_server_perm(token)
    return [asdict(guild, filter=filters.exclude(fields(hikari.OwnGuild).app))
            for guild in await UserService.find_mutual_guilds(guilds)]

