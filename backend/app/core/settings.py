
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "UAP OS"
    app_version: str = "0.1.0"

    database_url: str = "sqlite:///uap.db"

    host: str = "0.0.0.0"
    port: int = 8000

    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
