import typing as t

import hikari
from hikari.urls import OAUTH2_API_URL

from fastapi import (
    Depends,
    Response,
    Request
)
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer

from ..config import discord_config
from ..exceptions import UnauthorizedError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')


class TokenGrantPayload(t.TypedDict):
    client: str
    client_secret: str
    code: str
    redirect_uri: str


class TokenResponse(t.TypedDict):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str


class AuthService:
    app = hikari.RESTApp()

    @classmethod
    async def get_token_response(cls, payload: TokenGrantPayload) -> hikari.OAuth2AuthorizationToken:
        async with cls.app.acquire() as client:
            return await client.authorize_access_token(**payload)

    @classmethod
    async def logout(cls, token: str):
        async with cls.app.acquire() as client:
            await client.revoke_access_token(discord_config.client_id, discord_config.client_secret, token)

    @classmethod
    async def get_access_token(cls, code: str) -> hikari.OAuth2AuthorizationToken:
        payload: TokenGrantPayload = TokenGrantPayload(client=discord_config.client_id,
                                                       client_secret=discord_config.client_secret,
                                                       code=code,
                                                       redirect_uri=f"{discord_config.url}/auth/callback")
        return await cls.get_token_response(payload)

    @classmethod
    async def is_authenticated(cls, token: str):
        async with cls.app.acquire(token) as client:
            try:
                await client.fetch_authorization()
                return True
            except UnauthorizedError:
                return False

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
    def get_oauth_url(cls):
        scopes = f"scope={'%20'.join([hikari.OAuth2Scope.IDENTIFY, hikari.OAuth2Scope.GUILDS, hikari.OAuth2Scope.EMAIL])}"
        client_id = f"client_id={discord_config.client_id}"
        redirect_uri = f"redirect_uri={discord_config.url}/auth/callback"
        response_type = "response_type=code"
        return f"{OAUTH2_API_URL}/authorize?{response_type}&{client_id}&{scopes}&{redirect_uri}&prompt=consent"
