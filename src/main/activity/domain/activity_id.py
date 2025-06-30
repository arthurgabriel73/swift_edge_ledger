from uuid import UUID

class ActivityId:
    def __init__(self, activity_id: UUID):
        self._value = activity_id

    def value(self) -> UUID:
        return self._value