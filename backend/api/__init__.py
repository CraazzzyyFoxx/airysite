from fastapi import APIRouter
from starlette.responses import RedirectResponse

from . import (
    auth,
    user
)


router = APIRouter(prefix="/api/v1")


@router.get("/add-bot")
async def login():
    return RedirectResponse("https://discord.com/api/oauth2/authorize?client_id=669146461161914398&permissions=8"
                            "&scope=bot%20applications.commands")

router.include_router(auth.router)
router.include_router(user.router)
