from typing import Optional
from uuid import UUID

from src.main.activity.domain.activity_status import ActivityStatus


class ProcessActivityCommandOutput:
   def __init__(self, code: ActivityStatus, activity_id: Optional[UUID]):
    self.code = code
    self.activity_id = activity_id