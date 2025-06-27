
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main.shared.environment_settings import get_environment_variables

env = get_environment_variables()

DATABASE_URL = f'{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
