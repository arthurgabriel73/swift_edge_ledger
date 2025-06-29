from src.main.activity.domain.activity_status import ActivityStatus


class ProcessActivityCommandOutput:
   def __init__(self, code: ActivityStatus):
       self.code = code