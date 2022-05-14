from datetime import datetime

import hikari
from hikari.urls import OAUTH2_API_URL

from fastapi import (
    Depends,
)
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request
from cashews import cache
from passlib.hash import bcrypt

from ..config import discord_config, jwt_config
from ..exceptions import UnauthorizedError

from ..models.db import UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')


class AuthService:
    app = hikari.RESTApp()

    @classmethod
    async def get_tokens_from_response(cls, code: str, state: str) -> None:
        async with cls.app.acquire() as client:
            token = await client.authorize_access_token(client=discord_config.client_id,
                                                        client_secret=discord_config.client_secret,
                                                        code=code,
                                                        redirect_uri=f"{discord_config.url}/auth/callback")
            await cache.set(key=state, value=token, expire=3600)

    @classmethod
    async def logout(cls, token: str):
        async with cls.app.acquire() as client:
            await client.revoke_access_token(discord_config.client_id, discord_config.client_secret, token)

    @classmethod
    async def is_authenticated(cls, token: str):
        async with cls.app.acquire(token) as client:
            try:
                await client.fetch_authorization()
                return True
            except hikari.UnauthorizedError:
                raise UnauthorizedError from None

    @classmethod
    async def refresh_access_token(cls, refresh_token: str) -> hikari.OAuth2AuthorizationToken:
        async with cls.app.acquire() as client:
            return await client.refresh_access_token(discord_config.client_id,
                                                     discord_config.client_secret,
                                                     refresh_token)

    @classmethod
    async def requires_authorization(cls, token: str = Depends(oauth2_scheme)):
        return token

    @classmethod
    def get_oauth_url(cls, request: Request):
        state = bcrypt.hash(f"{request.headers.raw}")
        scopes = f"scope={'%20'.join([hikari.OAuth2Scope.IDENTIFY, hikari.OAuth2Scope.GUILDS])}"
        client_id = f"client_id={discord_config.client_id}"
        redirect_uri = f"redirect_uri={discord_config.url}/auth/callback"
        response_type = "response_type=code"
        return {"url": f"{OAUTH2_API_URL}/authorize?{response_type}&{client_id}&state={state}&{scopes}&{redirect_uri}&prompt=consent",
                "state": state}
