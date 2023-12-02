# Description: This file contains the routes for the sell.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.sell_controller import SellController

# Import types
from type.response_type import ResponseType
from type.sell_type import SellType, SellTypeUpdate

# Create the sell router instance
sell_controller: SellController = SellController()

# Create the sell router
sell_router: APIRouter = APIRouter(
    prefix="/api/sell",
    tags=["Sell"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all sells
@sell_router.get("/", response_model=ResponseType[list[SellType]])
async def get_all_sells():
    # Get the response
    response: ResponseType[list[SellType]] = sell_controller.get_all_sells()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a sell by id
@sell_router.get("/{fac_codigo}", response_model=ResponseType[SellType])
async def get_sell_by_id(fac_codigo: int):
    # Get the response
    response: ResponseType[SellType] = sell_controller.get_sell_by_id(fac_codigo)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create a sell
@sell_router.post("/", response_model=ResponseType)
async def create_sell(sell: SellType):
    # Get the response
    response: ResponseType = sell_controller.create_sell(sell)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update a sell
@sell_router.put("/", response_model=ResponseType)
async def update_sell(sell: SellTypeUpdate):
    # Get the response
    response: ResponseType = sell_controller.update_sell(sell)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete a sell
@sell_router.delete("/{fac_codigo}", response_model=ResponseType)
async def delete_sell(fac_codigo: int):
    # Get the response
    response: ResponseType = sell_controller.delete_sell(fac_codigo)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
