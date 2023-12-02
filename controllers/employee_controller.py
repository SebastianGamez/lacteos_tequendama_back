# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.employee_service import EmployeeService

# Importing types
from type.response_type import ResponseType
from type.employee_type import EmployeeType, EmployeeTypeUpdate


# Create the employee controller class
class EmployeeController:

    # Create constructor
    def __init__(self) -> None:
        self.employee_service: EmployeeService = EmployeeService()

    # Create method to get all employees
    def get_all_employees(self) -> ResponseType[list[EmployeeType]]:
        # Return the response type
        return self.employee_service.get_all_employees()

    # Create method to get a employee by id
    def get_employee_by_id(self, employee_id: int) -> ResponseType[EmployeeType]:
        # Return the response type
        return self.employee_service.get_employee_by_id(employee_id)

    # Create method to create a employee
    def create_employee(self, employee: EmployeeType) -> ResponseType:
        # Return the response type
        return self.employee_service.create_employee(employee)

    # Create method to update a employee
    def update_employee(self, employee: EmployeeTypeUpdate) -> ResponseType:
        # Return the response type
        return self.employee_service.update_employee(employee)

    # Create method to delete a employee
    def delete_employee(self, employee_id: int) -> ResponseType:
        # Return the response type
        return self.employee_service.delete_employee(employee_id)