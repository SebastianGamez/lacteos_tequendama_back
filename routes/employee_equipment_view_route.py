# Description: This file contains the routes for the employee equipment view.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.employee_equipment_view_controller import EmployeeEquipmentViewController

# Import types
from type.response_type import ResponseType
from type.employee_equipment_view_type import EmployeeEquipmentViewType

# Create the employee equipment view router instance
employee_equipment_view_controller: EmployeeEquipmentViewController = EmployeeEquipmentViewController()

# Create the employee equipment view router
employee_equipment_view_router: APIRouter = APIRouter(
    prefix="/api/employee_equipment_view",
    tags=["Employee Equipment View"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all employee equipment views
@employee_equipment_view_router.get("/", response_model=ResponseType[list[EmployeeEquipmentViewType]])
async def get_all_employee_equipment_views():
    # Get the response
    response: ResponseType[list[EmployeeEquipmentViewType]] = employee_equipment_view_controller.get_all_employee_equipment_view()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get an employee equipment view by employee id
@employee_equipment_view_router.get("/employee_id/{emp_id}", response_model=ResponseType[list[EmployeeEquipmentViewType]])
async def get_employee_equipment_view_by_employee_id(emp_id: int):
    # Get the response
    response: ResponseType[list[EmployeeEquipmentViewType]] = employee_equipment_view_controller.get_employee_equipment_view_by_employee_id(emp_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get an employee equipment view by equipment id
@employee_equipment_view_router.get("/equipment_id/{equ_id}", response_model=ResponseType[list[EmployeeEquipmentViewType]])
async def get_employee_equipment_view_by_equipment_id(equ_id: int):
    # Get the response
    response: ResponseType[list[EmployeeEquipmentViewType]] = employee_equipment_view_controller.get_employee_equipment_view_by_equipment_id(equ_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
