from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # Meta
    DEBUG: bool

    #  QFieldCLoud Config
    QFIELDCLOUD_URL: str
    QFIELDCLOUD_USERNAME: str
    QFIELDCLOUD_PASSWORD: str
    DEFAULT_PAGINATION_LIMIT: int = 10

    # Security
    ADMIN_API_TOKEN: str
    QFIELDCLOUD_TOKEN: str
