# Description: This file contains the routes for the inventory.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.inventory_controller import InventoryController

# Import types
from type.response_type import ResponseType
from type.inventory_type import InventoryType, InventoryTypeUpdate

# Create the inventory router instance
inventory_controller: InventoryController = InventoryController()

# Create the inventory router
inventory_router: APIRouter = APIRouter(
    prefix="/api/inventory",
    tags=["Inventory"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all inventories
@inventory_router.get("/", response_model=ResponseType[list[InventoryType]])
async def get_all_inventories():
    # Get the response
    response: ResponseType[list[InventoryType]] = inventory_controller.get_all_inventory()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get an inventory by id
@inventory_router.get("/{inv_id}", response_model=ResponseType[InventoryType])
async def get_inventory_by_id(inv_id: int):
    # Get the response
    response: ResponseType[InventoryType] = inventory_controller.get_inventory_by_id(inv_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create an inventory
@inventory_router.post("/", response_model=ResponseType)
async def create_inventory(inventory: InventoryType):
    # Get the response
    response: ResponseType = inventory_controller.create_inventory(inventory)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update an inventory
@inventory_router.put("/", response_model=ResponseType)
async def update_inventory(inventory: InventoryTypeUpdate):
    # Get the response
    response: ResponseType = inventory_controller.update_inventory(inventory)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete an inventory
@inventory_router.delete("/{inv_id}", response_model=ResponseType)
async def delete_inventory(inv_id: int):
    # Get the response
    response: ResponseType = inventory_controller.delete_inventory(inv_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response

