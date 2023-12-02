# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.sell_service import SellService

# Importing types
from type.response_type import ResponseType
from type.sell_type import SellType, SellTypeUpdate


# Create the sell controller class
class SellController:

    # Create constructor
    def __init__(self) -> None:
        self.sell_service: SellService = SellService()

    # Create method to get all sells
    def get_all_sells(self) -> ResponseType[list[SellType]]:
        # Return the response type
        return self.sell_service.get_all_sells()

    # Create method to get a sell by id
    def get_sell_by_id(self, fac_venta: int) -> ResponseType[SellType]:
        # Return the response type
        return self.sell_service.get_sell_by_id(fac_venta)

    # Create method to create a sell
    def create_sell(self, sell: SellType) -> ResponseType:
        # Return the response type
        return self.sell_service.create_sell(sell)

    # Create method to update a sell
    def update_sell(self, sell: SellTypeUpdate) -> ResponseType:
        # Return the response type
        return self.sell_service.update_sell(sell)

    # Create method to delete a sell
    def delete_sell(self, fac_codigo: int) -> ResponseType:
        # Return the response type
        return self.sell_service.delete_sell(fac_codigo)
