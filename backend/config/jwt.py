from pydantic import BaseSettings


class JwtConfig(BaseSettings):
    secret: str
    algorithm: str = 'HS256'
    expires_s: int = 3600

    class Config:
        env_file = ".env"
        env_prefix = "jwt_"


jwt_config = JwtConfig()
