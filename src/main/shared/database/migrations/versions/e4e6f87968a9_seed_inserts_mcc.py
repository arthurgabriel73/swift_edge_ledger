"""seed inserts mcc

Revision ID: e4e6f87968a9
Revises: f6b9e4b4d5e5
Create Date: 2025-06-29 23:49:17.868477

"""
import uuid
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.main.shared.database.sqlalchemy.models import CategoryEntity, MccEntity
from src.main.shared.date_util import get_utc_now
from src.main.shared.environment_settings import get_environment_variables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

env = get_environment_variables()

DATABASE_URL = f'{env.DATABASE_DIALECT}://{env.DATABASE_USER}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOST}:{env.DATABASE_PORT}/{env.DATABASE_NAME}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
# revision identifiers, used by Alembic.
revision: str = 'e4e6f87968a9'
down_revision: Union[str, Sequence[str], None] = 'f6b9e4b4d5e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    db = SessionLocal()
    categories = db.query(CategoryEntity).all()
    mcc_data = [
        {'code': '5411', 'category_id': next((c for c in categories if c.code == 'FOOD'), None).id},
        {'code': '5412', 'category_id': next((c for c in categories if c.code == 'FOOD'), None).id},
        {'code': '5811', 'category_id': next((c for c in categories if c.code == 'MEAL'), None).id},
        {'code': '5812', 'category_id': next((c for c in categories if c.code == 'MEAL'), None).id},
        {'code': '5815', 'category_id': next((c for c in categories if c.code == 'GROCERY'), None).id},
        {'code': '5816', 'category_id': next((c for c in categories if c.code == 'RESTAURANT'), None).id},
        {'code': '5817', 'category_id': next((c for c in categories if c.code == 'RESTAURANT'), None).id},
        {'code': '5818', 'category_id': next((c for c in categories if c.code == 'RESTAURANT'), None).id},
        {'code': '5819', 'category_id': next((c for c in categories if c.code == 'RESTAURANT'), None).id},
        {'code': '5912', 'category_id': next((c for c in categories if c.code == 'ENTERTAINMENT'), None).id},
    ]
    for mcc in mcc_data:
        mcc_entity = MccEntity(id=uuid.uuid4(),code=mcc['code'], category_id=int(mcc['category_id']), created_at=get_utc_now())
        db.add(mcc_entity)
        db.commit()
    db.close()


def downgrade() -> None:
    mcc_codes = [
        '5411',
        '5412',
        '5811',
        '5812',
        '5815',
        '5816',
        '5817',
        '5818',
        '5819',
        '5912'
    ]
    db = SessionLocal()
    for code in mcc_codes:
        db.query(MccEntity).filter_by(code=code).delete()
    db.commit()
    db.close()
