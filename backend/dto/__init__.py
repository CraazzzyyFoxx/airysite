import hikari
from attr import asdict, filters, fields


def dto_user(user: hikari.OwnUser):
    return asdict(user, filter=filters.exclude(fields(hikari.OwnUser).app))


def dto_guild(user: hikari.OwnGuild):
    return asdict(user, filter=filters.exclude(fields(hikari.OwnGuild).app))
