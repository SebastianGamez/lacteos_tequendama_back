# Description: This file contains the routes for the employee.
# Author: Sebastián Gámez Ariza

# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.employee_controller import EmployeeController

# Import types
from type.response_type import ResponseType
from type.employee_type import EmployeeType, EmployeeTypeUpdate

# Create the employee controller instance
employee_controller: EmployeeController = EmployeeController()

# Create the employee router
employee_router: APIRouter = APIRouter(
    prefix="/api/employee",
    tags=["Employee"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all employees
@employee_router.get("/", response_model=ResponseType[list[EmployeeType]])
async def get_all_employees():
    # Get the response
    response: ResponseType[list[EmployeeType]] = employee_controller.get_all_employees()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a employee by id
@employee_router.get("/{employee_id}", response_model=ResponseType[EmployeeType])
async def get_employee_by_id(employee_id: int) -> ResponseType[EmployeeType]:
    # Get the response
    response: ResponseType[EmployeeType] = employee_controller.get_employee_by_id(employee_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create a employee
@employee_router.post("/", response_model=ResponseType)
async def create_employee(employee: EmployeeType) -> ResponseType:
    # Get the response
    response: ResponseType = employee_controller.create_employee(employee)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update a employee
@employee_router.put("/", response_model=ResponseType)
async def update_employee(employee: EmployeeTypeUpdate) -> ResponseType:
    # Get the response
    response: ResponseType = employee_controller.update_employee(employee)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete a employee
@employee_router.delete("/{employee_id}", response_model=ResponseType)
async def delete_employee(employee_id: int) -> ResponseType:
    # Get the response
    response: ResponseType = employee_controller.delete_employee(employee_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
