from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main.shared.environment_settings import get_environment_variables
from src.main.shared.database.sqlalchemy.models import Base
from src.main.main import app

env = get_environment_variables()

DATABASE_URL = f'{env.DATABASE_DIALECT}://{env.DATABASE_USER}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOST}:{env.DATABASE_PORT}/{env.DATABASE_NAME}'

engine = create_engine(DATABASE_URL)

TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def before_all(context):
    context.client = TestClient(app)

def before_scenario(context, scenario):
    Base.metadata.create_all(bind=engine)
    context.db = TestingSessionLocal()

def after_scenario(context, scenario):
    context.db.close()
    Base.metadata.drop_all(bind=engine)

def after_all(context):
    context.client.close()


