# Description: This file handles the database connection related with the employee
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.employee_type import EmployeeType, EmployeeTypeUpdate
from type.response_type import ResponseType


# Create the employee services class
class EmployeeService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all employees
    def get_all_employees(self) -> ResponseType[list[EmployeeType]]:
        # Create the response type
        response_type: ResponseType[list[EmployeeType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from empleado"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employees found successfully",
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

    # Create method to get an employee by id
    def get_employee_by_id(self, emp_id: int) -> ResponseType[EmployeeType]:
        # Create the response type
        response_type: ResponseType[EmployeeType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                employee, *_ = conn.execute(text("select * from empleado where emp_id = :id"), {"id": emp_id})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employee found successfully",
                    data=employee
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

    # Create method to create an employee
    def create_employee(self, employee: EmployeeType) -> ResponseType:
        # Create the response type
        response_type: ResponseType[EmployeeType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(
                    text("insert into empleado(emp_nombre, emp_apellido, emp_telefono, emp_direccion, emp_correo, emp_cargo) values (:emp_nombre, :emp_apellido, :emp_telefono, :emp_direccion, :emp_correo, :emp_cargo)"),
                    {
                        "emp_nombre": employee.emp_nombre,
                        "emp_apellido": employee.emp_apellido,
                        "emp_telefono": employee.emp_telefono,
                        "emp_direccion": employee.emp_direccion,
                        "emp_correo": employee.emp_correo,
                        "emp_cargo": employee.emp_cargo
                    }
                )
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employee created successfully"
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

    # Create method to update an employee
    def update_employee(self, employee: EmployeeTypeUpdate) -> ResponseType:
        # Create the response type
        response_type: ResponseType[EmployeeTypeUpdate]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                for employee_key, employee_value in employee.dict(exclude_none=True).items():
                    # Execute the query
                    conn.execute(
                        text(f"update empleado set {employee_key} = :value where emp_id = :id"),
                        {
                            "value": employee_value,
                            "id": employee.emp_id
                        }
                    )
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employee updated successfully"
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

    # Create method to delete an employee
    def delete_employee(self, emp_id: int) -> ResponseType:
        # Create the response type
        response_type: ResponseType[EmployeeType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("delete from empleado where emp_id = :id"), {"id": emp_id})
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Employee deleted successfully"
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
