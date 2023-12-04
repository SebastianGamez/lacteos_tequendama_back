# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.procedures_service import ProceduresService

# Importing types
from type.response_type import ResponseType
from type.register_buy_type import RegisterBuyType
from type.register_sell_type import RegisterSellType
from type.update_inventory_type import UpdateInventoryType


# Create the procedures controller class
class ProceduresController:

    # Create constructor
    def __init__(self) -> None:
        self.procedures_service: ProceduresService = ProceduresService()

    # Create method to register a buy
    def register_buy(self, register_buy: RegisterBuyType) -> ResponseType:
        return self.procedures_service.register_buy(register_buy)

    # Create method to register a sell
    def register_sell(self, register_sell: RegisterSellType) -> ResponseType:
        return self.procedures_service.register_sell(register_sell)

    # Create method to update inventory
    def update_inventory(self, update_inventory: UpdateInventoryType) -> ResponseType:
        return self.procedures_service.update_inventory(update_inventory)
