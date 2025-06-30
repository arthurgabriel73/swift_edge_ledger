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
    APP_NAME: Optional[str] = Field(validation_alias='APP_NAME_VALUE') or 'swift_edge_ledger'
    APP_HOST: Optional[str] = Field(validation_alias='APP_HOST_VALUE') or '0.0.0.0'
    APP_PORT: Optional[int] = Field(validation_alias='APP_PORT_VALUE') or '3000'
    DATABASE_DIALECT: Optional[str] = Field(validation_alias='DATABASE_DIALECT_VALUE') or 'postgresql+psycopg'
    DATABASE_HOST: Optional[str] = Field(validation_alias='DATABASE_HOST_VALUE') or 'localhost'
    DATABASE_NAME: Optional[str] = Field(validation_alias='DATABASE_NAME_VALUE') or 'swift_edge_ledger_db'
    DATABASE_PASSWORD: Optional[str] = Field(validation_alias='DATABASE_PASSWORD_VALUE') or 'password'
    DATABASE_PORT: Optional[int] = Field(validation_alias='DATABASE_PORT_VALUE') or '5432'
    DATABASE_USER: Optional[str] = Field(validation_alias='DATABASE_USER_VALUE') or 'postgres'
    model_config = SettingsConfigDict(
        env_file=get_env_filename(), env_ignore_empty=True, populate_by_name=True, extra='allow'
    )


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
