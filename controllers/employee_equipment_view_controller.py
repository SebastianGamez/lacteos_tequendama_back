# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.employee_equipment_view_service import EmployeeEquipmentViewService

# Importing types
from type.response_type import ResponseType
from type.employee_equipment_view_type import EmployeeEquipmentViewType


# Create the employee equipment view controller class
class EmployeeEquipmentViewController:

    # Create constructor
    def __init__(self) -> None:
        self.employee_equipment_view_service: EmployeeEquipmentViewService = EmployeeEquipmentViewService()

    # Create method to get all employee equipment view
    def get_all_employee_equipment_view(self) -> ResponseType[list[EmployeeEquipmentViewType]]:
        # Return the response type
        return self.employee_equipment_view_service.get_all_employee_equipment_view()

    # Create method to get an employee equipment view by employee id
    def get_employee_equipment_view_by_employee_id(self, emp_id: int) -> ResponseType[list[EmployeeEquipmentViewType]]:
        # Return the response type
        return self.employee_equipment_view_service.get_employee_equipment_view_by_employee_id(emp_id)

    # Create method to get an employee equipment view by equipment id
    def get_employee_equipment_view_by_equipment_id(self, equ_id: int) -> ResponseType[list[EmployeeEquipmentViewType]]:
        # Return the response type
        return self.employee_equipment_view_service.get_employee_equipment_view_by_equipment_id(equ_id)
