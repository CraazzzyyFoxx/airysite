import typing as t

import hikari
from hikari import OwnGuild

from backend.utils.helpers import includes_permissions
from backend.config import discord_config


class UserService:
    app = hikari.RESTApp()

    @classmethod
    async def fetch_user(cls, token: str) -> hikari.OwnUser:
        async with cls.app.acquire(token) as client:
            return await client.fetch_my_user()

    @classmethod
    async def fetch_guilds(cls, token: str) -> t.Sequence[OwnGuild]:
        async with cls.app.acquire(token) as client:
            return await client.fetch_my_guilds()

    @classmethod
    async def fetch_guilds_for_dashboard(cls, token: str) -> t.Sequence[OwnGuild]:
        async with cls.app.acquire(token) as client:
            guilds = await client.fetch_my_guilds()
            return [guild for guild in guilds if
                    includes_permissions(guild.my_permissions,
                                         hikari.Permissions.MANAGE_GUILD | hikari.Permissions.ADMINISTRATOR)]

    @classmethod
    async def fetch_mutual_guilds(cls, guilds: t.Sequence[OwnGuild]):
        async with cls.app.acquire(discord_config.token, token_type=hikari.TokenType.BOT) as client:
            my_guilds = await client.fetch_my_guilds()
        return [guild for guild in guilds if guild in my_guilds]
