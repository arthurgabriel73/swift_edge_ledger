from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID


class MerchantGateway(ABC):

    @abstractmethod
    def find_merchant_id_by_name(self, merchant_name: str) -> Optional[UUID]:
        """
        Finds the merchant ID associated with a given merchant name.

        :param merchant_name: The name of the merchant.
        :return: The ID of the merchant if found, otherwise None.
        """
        pass

    @abstractmethod
    def get_category_id_by_merchant(self, merchant_name: str) -> Optional[int]:
        """
        Retrieves the category ID associated with a given merchant name.

        :param merchant_name: The name of the merchant.
        :return: The category ID associated with the merchant.
        """
        pass

    @abstractmethod
    def get_category_id_by_mcc(self, mcc: str) -> Optional[int]:
        """
        Retrieves the category ID associated with a given MCC (Merchant Category Code).

        :param mcc: The Merchant Category Code.
        :return: The category ID associated with the MCC.
        """
        pass

    @abstractmethod
    def get_category_id_by_code(self, code: str) -> Optional[int]:
        """
        Retrieves the category ID associated with a given category code.

        :param code: The category code.
        :return: The category ID associated with the code.
        """
        pass