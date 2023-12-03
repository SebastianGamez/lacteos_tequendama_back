# Description: This file handles the database connection related with the employee equipment view
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.employee_equipment_view_type import EmployeeEquipmentViewType


# Create the employee equipment view services class
class EmployeeEquipmentViewService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all employee equipment view
    def get_all_employee_equipment_view(self) -> ResponseType[list[EmployeeEquipmentViewType]]:
        # Create the response type
        response_type: ResponseType[list[EmployeeEquipmentViewType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from vista_empleados_con_equipamiento"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employee equipment view found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to get an employee equipment view by employee id
    def get_employee_equipment_view_by_employee_id(self, emp_id: int) -> ResponseType[list[EmployeeEquipmentViewType]]:
        # Create the response type
        response_type: ResponseType[list[EmployeeEquipmentViewType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from vista_empleados_con_equipamiento where emp_id = :id"), {"id": emp_id})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employee equipment view found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to get an employee equipment view by equipment id
    def get_employee_equipment_view_by_equipment_id(self, equ_id: int) -> ResponseType[list[EmployeeEquipmentViewType]]:
        # Create the response type
        response_type: ResponseType[list[EmployeeEquipmentViewType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from vista_empleados_con_equipamiento where equ_id = :id"), {"id": equ_id})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employee equipment view found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type
