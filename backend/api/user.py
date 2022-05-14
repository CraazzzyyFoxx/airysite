from pprint import pprint

from fastapi import (
    APIRouter,
    Depends,
)
from starlette.responses import JSONResponse

from backend.dto import dto_user, dto_guild
from backend.services import (
    AuthService,
    UserService
)


router = APIRouter(
    prefix='/users',
    tags=['user'],
)


@router.post("/@me")
async def get_user(token=Depends(AuthService.requires_authorization)):
    user = await UserService.fetch_user(token)
    return dto_user(user)


@router.post(
    "/guilds",
    dependencies=[Depends(AuthService.requires_authorization)],
)
async def fetch_guilds(token=Depends(AuthService.requires_authorization)):
    return [dto_guild(guild) for guild in await UserService.fetch_guilds(token)]


@router.post(
    "/guilds/dashboard",
    dependencies=[Depends(AuthService.requires_authorization)],
)
async def get_guilds_bot_master(token=Depends(AuthService.requires_authorization)):
    guilds = await UserService.fetch_guilds_for_dashboard(token)
    mutual_guilds = await UserService.fetch_mutual_guilds(guilds)
    prepared_guilds = []
    for guild in guilds:
        data = dto_guild(guild)
        if guild in mutual_guilds:
            data["is_mutual"] = True
        else:
            data["is_mutual"] = False
        prepared_guilds.append(data)
    return JSONResponse(prepared_guilds)


