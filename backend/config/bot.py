from pydantic import BaseSettings, UUID4


class BotConfig(BaseSettings):
    secret: UUID4

    class Config:
        env_file = ".env"
        env_prefix = "bot_"


bot_config = BotConfig()
