import attr
import hikari


@attr.define(kw_only=True)
class MutualGuild(hikari.OwnGuild):
    is_mutual: bool
