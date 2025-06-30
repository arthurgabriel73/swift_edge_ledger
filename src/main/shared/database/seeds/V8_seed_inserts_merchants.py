"""seed inserts merchants

Revision ID: a3ea37d4c3cc
Revises: e4e6f87968a9
Create Date: 2025-06-29 23:59:29.320114

"""
import uuid
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.main.shared.database.sqlalchemy.models import MccEntity, MerchantEntity
from src.main.shared.date_util import get_utc_now
from src.main.shared.environment_settings import get_environment_variables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision: str = 'a3ea37d4c3cc'
down_revision: Union[str, Sequence[str], None] = 'e4e6f87968a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

env = get_environment_variables()

DATABASE_URL = f'{env.DATABASE_DIALECT}://{env.DATABASE_USER}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOST}:{env.DATABASE_PORT}/{env.DATABASE_NAME}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def upgrade() -> None:
    db = SessionLocal()
    mcc_entities = db.query(MccEntity).all()
    merchant_data = [
        {'name': 'UBER TRIP SAO PAULO BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5411'), None)},
        {'name': 'UBER EATS SAO PAULO BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5412'), None)},
        {'name': 'PAG*JoseDaSilva RIO DE JANEI BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5811'), None)},
        {'name': 'PICPAY*BILHETEUNICO GOIANIA BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5812'), None)},
        {'name': 'PICPAY*BILHETEUNICO SAO PAULO BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5812'), None)},
        {'name': 'PICPAY*BILHETEUNICO RIO DE JANEIRO BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5812'), None)},
        {'name': 'PICPAY*BILHETEUNICO CURITIBA BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5812'), None)},
        {'name': 'PICPAY*BILHETEUNICO PORTO ALEGRE BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5812'), None)},
        {'name': 'PICPAY*BILHETEUNICO SALVADOR BR', 'mcc_id': next((mcc.id for mcc in mcc_entities if mcc.code == '5812'), None)},
    ]

    for merchant in merchant_data:
        merchant_entity = MerchantEntity(
            id=uuid.uuid4(),
            merchant_name=merchant['name'],
            mcc_id=str(merchant['mcc_id']), # necessary to convert UUID to string for the database
            created_at=get_utc_now()
        )
        db.add(merchant_entity)
        db.commit()
    db.close()


def downgrade() -> None:
    db = SessionLocal()
    merchant_names = [
        'UBER TRIP SAO PAULO BR',
        'UBER EATS SAO PAULO BR',
        'PAG*JoseDaSilva RIO DE JANEI BR',
        'PICPAY*BILHETEUNICO GOIANIA BR',
        'PICPAY*BILHETEUNICO SAO PAULO BR',
        'PICPAY*BILHETEUNICO RIO DE JANEIRO BR',
        'PICPAY*BILHETEUNICO CURITIBA BR',
        'PICPAY*BILHETEUNICO PORTO ALEGRE BR',
        'PICPAY*BILHETEUNICO SALVADOR BR',
    ]

    for name in merchant_names:
        db.query(MerchantEntity).filter(MerchantEntity.merchant_name == name).delete()

    db.commit()
    db.close()
