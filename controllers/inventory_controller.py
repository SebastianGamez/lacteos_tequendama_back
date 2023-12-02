# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.inventory_service import InventoryService

# Importing types
from type.response_type import ResponseType
from type.inventory_type import InventoryType, InventoryTypeUpdate


# Create the inventory controller class
class InventoryController:

    # Create constructor
    def __init__(self) -> None:
        self.inventory_service: InventoryService = InventoryService()

    # Create method to get all inventory
    def get_all_inventory(self) -> ResponseType[list[InventoryType]]:
        # Return the response type
        return self.inventory_service.get_all_inventory()

    # Create method to get an inventory by id
    def get_inventory_by_id(self, inv_id: int) -> ResponseType[InventoryType]:
        # Return the response type
        return self.inventory_service.get_inventory_by_id(inv_id)

    # Create method to create an inventory
    def create_inventory(self, inventory: InventoryType) -> ResponseType:
        # Return the response type
        return self.inventory_service.create_inventory(inventory)

    # Create method to update an inventory
    def update_inventory(self, inventory: InventoryTypeUpdate) -> ResponseType:
        # Return the response type
        return self.inventory_service.update_inventory(inventory)

    # Create method to delete an inventory
    def delete_inventory(self, inv_id: int) -> ResponseType:
        # Return the response type
        return self.inventory_service.delete_inventory(inv_id)
    