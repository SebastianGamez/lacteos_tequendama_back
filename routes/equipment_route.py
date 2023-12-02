# Description: This file contains the routes for the equipment.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.equipment_controller import EquipmentController

# Import types
from type.response_type import ResponseType
from type.equipment_type import EquipmentType, EquipmentTypeUpdate

# Create the equipment router instance
equipment_controller: EquipmentController = EquipmentController()

# Create the equipment router
equipment_router: APIRouter = APIRouter(
    prefix="/api/equipment",
    tags=["Equipment"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all equipment
@equipment_router.get("/", response_model=ResponseType[list[EquipmentType]])
async def get_all_equipment():
    # Get the response
    response: ResponseType[list[EquipmentType]] = equipment_controller.get_all_equipment()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get an equipment by id
@equipment_router.get("/{equ_id}", response_model=ResponseType[EquipmentType])
async def get_equipment_by_id(equ_id: int):
    # Get the response
    response: ResponseType[EquipmentType] = equipment_controller.get_equipment_by_id(equ_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create an equipment
@equipment_router.post("/", response_model=ResponseType)
async def create_equipment(equipment: EquipmentType):
    # Get the response
    response: ResponseType = equipment_controller.create_equipment(equipment)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update an equipment
@equipment_router.put("/", response_model=ResponseType)
async def update_equipment(equipment: EquipmentTypeUpdate):
    # Get the response
    response: ResponseType = equipment_controller.update_equipment(equipment)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete an equipment
@equipment_router.delete("/{equ_id}", response_model=ResponseType)
async def delete_equipment(equ_id: int):
    # Get the response
    response: ResponseType = equipment_controller.delete_equipment(equ_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response

