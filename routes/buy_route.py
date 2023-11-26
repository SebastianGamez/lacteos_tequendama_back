# Description: This file contains the routes for the buy.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.buy_controller import BuyController

# Import types
from type.response_type import ResponseType
from type.buy_type import BuyType, BuyTypeUpdate

# Create the buy controller instance
buy_controller: BuyController = BuyController()

# Create the buy router
buy_router: APIRouter = APIRouter(
    prefix="/api/buy",
    tags=["Buy"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all buys
@buy_router.get("/", response_model=ResponseType[list[BuyType]])
async def get_all_buys():
    # Get the response
    response: ResponseType[list[BuyType]] = buy_controller.get_all_buys()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a buy by id
@buy_router.get("/{buy_id}", response_model=ResponseType[BuyType])
async def get_buy_by_id(buy_id: int) -> ResponseType[BuyType]:
    # Get the response
    response: ResponseType[BuyType] = buy_controller.get_buy_by_id(buy_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create a buy
@buy_router.post("/", response_model=ResponseType)
async def create_buy(buy: BuyType) -> ResponseType:
    # Get the response
    response: ResponseType = buy_controller.create_buy(buy)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update a buy
@buy_router.put("/", response_model=ResponseType)
async def update_buy(buy: BuyTypeUpdate) -> ResponseType:
    # Get the response
    response: ResponseType = buy_controller.update_buy(buy)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete a buy
@buy_router.delete("/{buy_id}", response_model=ResponseType)
async def delete_buy(buy_id: int) -> ResponseType:
    # Get the response
    response: ResponseType = buy_controller.delete_buy(buy_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    return response
