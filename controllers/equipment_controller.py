# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.equipment_service import EquipmentService

# Importing types
from type.response_type import ResponseType
from type.equipment_type import EquipmentType, EquipmentTypeUpdate


# Create the equipment controller class
class EquipmentController:

    # Create constructor
    def __init__(self) -> None:
        self.equipment_service: EquipmentService = EquipmentService()

    # Create method to get all equipments
    def get_all_equipment(self) -> ResponseType[list[EquipmentType]]:
        # Return the response type
        return self.equipment_service.get_all_equipment()

    # Create method to get an equipment by id
    def get_equipment_by_id(self, equ_id: int) -> ResponseType[EquipmentType]:
        # Return the response type
        return self.equipment_service.get_equipment_by_id(equ_id)

    # Create method to create an equipment
    def create_equipment(self, equipment: EquipmentType) -> ResponseType:
        # Return the response type
        return self.equipment_service.create_equipment(equipment)

    # Create method to update an equipment
    def update_equipment(self, equipment: EquipmentTypeUpdate) -> ResponseType:
        # Return the response type
        return self.equipment_service.update_equipment(equipment)

    # Create method to delete an equipment
    def delete_equipment(self, equ_id: int) -> ResponseType:
        # Return the response type
        return self.equipment_service.delete_equipment(equ_id)