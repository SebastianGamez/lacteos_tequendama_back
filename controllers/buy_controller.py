# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.buy_service import BuyService

# Importing types
from type.response_type import ResponseType
from type.buy_type import BuyType, BuyTypeUpdate


# Create the buy controller class
class BuyController:

    # Create constructor
    def __init__(self) -> None:
        self.buy_service: BuyService = BuyService()

    # Create method to get all buys
    def get_all_buys(self) -> ResponseType[list[BuyType]]:
        # Return the response type
        return self.buy_service.get_all_buys()

    # Create method to get a buy by id
    def get_buy_by_id(self, buy_id: int) -> ResponseType[BuyType]:
        # Return the response type
        return self.buy_service.get_buy_by_id(buy_id)

    # Create method to create a buy
    def create_buy(self, buy: BuyType) -> ResponseType:
        # Return the response type
        return self.buy_service.create_buy(buy)

    # Create method to update a buy
    def update_buy(self, buy: BuyTypeUpdate) -> ResponseType:
        # Return the response type
        return self.buy_service.update_buy(buy)

    # Create method to delete a buy
    def delete_buy(self, buy_id: int) -> ResponseType:
        # Return the response type
        return self.buy_service.delete_buy(buy_id)
