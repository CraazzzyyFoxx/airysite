from fastapi import APIRouter
from starlette.responses import RedirectResponse
from backend.config import discord_config

from . import (
    auth,
    user
)


router = APIRouter(prefix="/api/v1")


@router.get("/add-bot")
async def login():
    return RedirectResponse(f"https://discord.com/api/oauth2/authorize?client_id={discord_config.client_id}&permissions=8 "
                            "&scope=bot%20applications.commands&redirect_uri=https://crypto.asuscomm.com:80/dashboard")


@router.get("/add-bot/{guild_id}")
async def login(guild_id: int):
    return RedirectResponse(f"https://discord.com/api/oauth2/authorize?client_id={discord_config.client_id}&guild_id={guild_id}"
                            f"&permissions=8&scope=bot%20applications.commands&redirect_uri=https://crypto.asuscomm.com:80/dashboard")

router.include_router(auth.router)
router.include_router(user.router)
