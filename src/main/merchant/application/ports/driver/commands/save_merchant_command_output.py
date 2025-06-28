from src.main.merchant.domain.merchant_id import MerchantId
from src.main.merchant.domain.merchant_name import MerchantName


class SaveMerchantCommandOutput:
    def __init__(self, merchant_id: MerchantId, merchant_name: MerchantName):
        self.merchant_id = merchant_id.value().hex
        self.merchant_name = merchant_name.value()