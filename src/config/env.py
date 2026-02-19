from pydantic.config import BaseSettings


class AppEnv(BaseSettings):
    DEBUG: bool
