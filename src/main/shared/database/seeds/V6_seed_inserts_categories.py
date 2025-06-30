"""seed inserts categories

Revision ID: f6b9e4b4d5e5
Revises: 651a0ff84de6
Create Date: 2025-06-29 23:33:14.703200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import session

from src.main.shared.database.sqlalchemy.models import CategoryEntity
from src.main.shared.date_util import get_utc_now
from src.main.shared.environment_settings import get_environment_variables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision: str = 'f6b9e4b4d5e5'
down_revision: Union[str, Sequence[str], None] = '651a0ff84de6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

env = get_environment_variables()

DATABASE_URL = f'{env.DATABASE_DIALECT}://{env.DATABASE_USER}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOST}:{env.DATABASE_PORT}/{env.DATABASE_NAME}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def upgrade() -> None:
    db = SessionLocal()
    category = [
        {'code': 'CASH', 'description': 'CASH CATEGORY'},
        {'code': 'FOOD', 'description': 'FOOD CATEGORY'},
        {'code': 'MEAL', 'description': 'MEAL CATEGORY'},
        {'code': 'GROCERY', 'description': 'GROCERY CATEGORY'},
        {'code': 'RESTAURANT', 'description': 'RESTAURANT CATEGORY'},
        {'code': 'ENTERTAINMENT', 'description': 'ENTERTAINMENT CATEGORY'},
    ]

    for c in category:
        category = CategoryEntity(code=c['code'], description=c['description'], created_at=get_utc_now())
        db.add(category)
        db.commit()
    db.close()


def downgrade() -> None:
    db = SessionLocal()
    category = [
        {'code': 'CASH', 'description': 'CASH CATEGORY'},
        {'code': 'FOOD', 'description': 'FOOD CATEGORY'},
        {'code': 'MEAL', 'description': 'MEAL CATEGORY'},
        {'code': 'GROCERY', 'description': 'GROCERY CATEGORY'},
        {'code': 'RESTAURANT', 'description': 'RESTAURANT CATEGORY'},
        {'code': 'ENTERTAINMENT', 'description': 'ENTERTAINMENT CATEGORY'},
    ]

    for c in category:
        db.query(CategoryEntity).filter_by(code=c['code']).delete()
    db.commit()
    db.close()