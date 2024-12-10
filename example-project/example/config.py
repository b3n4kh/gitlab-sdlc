from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    APPLICATION_ROOT: str = "/"
    MODULE_ID: str = "Example"
    DEBUG: bool = False


Config = Settings()
