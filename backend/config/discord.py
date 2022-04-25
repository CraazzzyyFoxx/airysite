from pydantic import BaseSettings


class DiscordConfig(BaseSettings):
    client_id: int
    client_secret: str
    token: str
    url: str

    class Config:
        env_file = ".env"
        env_prefix = "discord_"


discord_config = DiscordConfig()
