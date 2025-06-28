from uuid import UUID


class SaveMerchantCommand:
    def __init__(self, merchant_name: str, mcc_id: UUID):
        SaveMerchantCommand.validate_merchant_name(merchant_name)
        SaveMerchantCommand.validate_mcc_id(mcc_id)
        self.merchant_name = merchant_name
        self.mcc_id = mcc_id

    @staticmethod
    def validate_merchant_name(merchant_name: str):
        if not merchant_name or not isinstance(merchant_name, str):
            raise ValueError("Invalid merchant name")
        if len(merchant_name) < 3 or len(merchant_name) > 100:
            raise ValueError("Merchant name must be between 3 and 100 characters long")

    @staticmethod
    def validate_mcc_id(mcc_id: UUID):
        if not isinstance(mcc_id, UUID):
            raise ValueError("Invalid MCC ID")
