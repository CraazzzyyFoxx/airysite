import typing as t

import hikari
from attr import fields
from attrs import filters, asdict
from fastapi import (
    APIRouter,
    Depends,
    Request,
)
from starlette.responses import RedirectResponse, JSONResponse

from backend.exceptions import UnauthorizedError
from backend.services.auth import (
    AuthService, oauth2_scheme
)
from backend.services.user import UserService


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.get("/login")
async def login(auth_service: AuthService = Depends(),):
    return RedirectResponse(auth_service.get_oauth_url())


@router.post("/logout")
async def logout(request: Request, auth_service: AuthService = Depends(), token: str = Depends(oauth2_scheme)):
    try:
        request.cookies.pop('refreshToken')
    except KeyError:
        pass
    await auth_service.logout(token)


@router.get("/callback")
async def callback(code: str, auth_service: AuthService = Depends(), state: t.Optional[str] = None):
    token = await auth_service.get_access_token(code)

    user = await UserService.fetch_user(token.access_token)
    resp = RedirectResponse("http://crypto.asuscomm.com:3000/")
    # resp = JSONResponse({"user": asdict(user, filter=filters.exclude(fields(hikari.OwnUser).app)),
    #                      "accessToken": token.access_token,
    #                      "refreshToken": token.refresh_token})
    resp.set_cookie('refreshToken',
                    token.refresh_token.__str__(),
                    expires=int(token.expires_in.total_seconds()),
                    httponly=True)
    print(token, token.access_token)
    return resp


@router.get("/refresh")
async def is_authenticated(request: Request, auth_service: AuthService = Depends()):
    token = request.cookies.get("refreshToken")
    token = await auth_service.refresh_access_token(token)
    resp = JSONResponse({"accessToken": token.access_token, "refreshToken": token.refresh_token})
    resp.set_cookie('refreshToken',
                    token.refresh_token.__str__(),
                    expires=int(token.expires_in.total_seconds()),
                    httponly=True)
    return resp
