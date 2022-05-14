import typing as t

from cashews import cache
from fastapi import (
    APIRouter,
    Depends,
    Request,
)
from passlib.hash import bcrypt
from starlette import status
from starlette.responses import JSONResponse

from backend.config import jwt_config
from backend.dto import dto_user
from backend.exceptions import APIError
from backend.services import UserService
from backend.services.auth import (
    AuthService, oauth2_scheme
)


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.get("/login")
async def login(request: Request, auth_service: AuthService = Depends(),):
    return JSONResponse(auth_service.get_oauth_url(request))


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(auth_service: AuthService = Depends(), token: str = Depends(oauth2_scheme)):
    await auth_service.logout(token)
    resp = JSONResponse({'status': "Success"})
    resp.delete_cookie(key='refreshToken')
    return resp


@router.get("/callback", status_code=status.HTTP_200_OK)
async def callback(code: str, auth_service: AuthService = Depends(), state: str = None):
    await auth_service.get_tokens_from_response(code, state)


@router.get("/finalize-login", status_code=status.HTTP_200_OK)
async def callback(user_service: UserService = Depends(), state: str = None):
    token = await cache.get(state, None)
    if not token:
        raise APIError(status_code=status.HTTP_408_REQUEST_TIMEOUT) from None
    user = await user_service.fetch_user(token.access_token)
    resp = JSONResponse({"user": dto_user(user),
                         "accessToken": token.access_token,
                         "refreshToken": token.refresh_token})
    resp.set_cookie('refreshToken',
                    token.refresh_token.__str__(),
                    expires=int(token.expires_in.total_seconds()),
                    httponly=True,
                    secure=True)
    return resp


@router.get("/refresh")
async def is_authenticated(request: Request, auth_service: AuthService = Depends()):
    token = request.cookies.get("refreshToken")
    token = await auth_service.refresh_access_token(token)
    resp = JSONResponse({"accessToken": token.access_token, "refreshToken": token.refresh_token})
    resp.set_cookie('refreshToken',
                    token.refresh_token.__str__(),
                    expires=int(token.expires_in.total_seconds()),
                    httponly=True,
                    secure=True)
    return resp
