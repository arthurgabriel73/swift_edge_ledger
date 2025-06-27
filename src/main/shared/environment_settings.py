import os
from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache
def get_env_filename():
    runtime_env = os.getenv('ENV')
    return f'.env.{runtime_env}' if runtime_env else '.env'


class EnvironmentSettings(BaseSettings):
    APP_NAME: Optional[str] = Field(validation_alias='APP_NAME_VALUE') or None
    APP_HOST: Optional[str] = Field(validation_alias='APP_HOST_VALUE') or None
    APP_PORT: Optional[int] = Field(validation_alias='APP_PORT_VALUE') or None
    DATABASE_DIALECT: Optional[str] = Field(validation_alias='DATABASE_DIALECT_VALUE') or None
    DATABASE_HOST: Optional[str] = Field(validation_alias='DATABASE_HOST_VALUE') or None
    DATABASE_NAME: Optional[str] = Field(validation_alias='DATABASE_NAME_VALUE') or None
    DATABASE_PASSWORD: Optional[str] = Field(validation_alias='DATABASE_PASSWORD_VALUE') or None
    DATABASE_PORT: Optional[int] = Field(validation_alias='DATABASE_PORT_VALUE') or None
    DATABASE_USER: Optional[str] = Field(validation_alias='DATABASE_USER_VALUE') or None
    model_config = SettingsConfigDict(
        env_file=get_env_filename(), env_ignore_empty=True, populate_by_name=True, extra='allow'
    )


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
