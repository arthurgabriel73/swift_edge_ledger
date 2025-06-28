from src.main.merchant.domain.mcc_id import MccId


class SaveMccCommandOutput:
    def __init__(self, mcc_id: MccId, code: str, category_id: int):
        self.mcc_id = mcc_id.value().hex
        self.code = code
        self.category_id = category_id