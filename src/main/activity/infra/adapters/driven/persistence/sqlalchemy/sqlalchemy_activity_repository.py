from typing import Optional

from sqlalchemy import Table
from sqlalchemy.orm import Session

from src.main.activity.application.ports.driven.activity_repository import ActivityRepository
from src.main.activity.domain.activity import Activity
from src.main.activity.domain.activity_id import ActivityId
from src.main.shared.database.sqlalchemy.models import ActivityEntity
from src.main.shared.persistence_decorators import repository


@repository
class SqlAlchemyActivityRepository(ActivityRepository):
    def save(self, activity: Activity, session: Optional[Session] = None) -> Activity:
        if session is None:
            raise ValueError("Session must be provided for saving the activity.")
        activity_entity = ActivityEntity.from_domain(activity)
        table = Table('activities', ActivityEntity.metadata)
        session.execute(table.insert(), [activity_entity.to_dict()])
        return activity_entity.to_domain()

    def find_by_id(self, activity_id: ActivityId, session: Optional[Session] = None) -> Optional[Activity]:
        if session is None:
            raise ValueError("Session must be provided for finding the activity by ID.")

        query = session.query(ActivityEntity).where(ActivityEntity.id == activity_id.value())
        activity_entity = session.execute(query).scalars().unique().one_or_none()
        if activity_entity is None:
            return None
        return activity_entity.to_domain()