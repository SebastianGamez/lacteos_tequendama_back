# Description: This file contains the routes for the procedures.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.procedures_controller import ProceduresController

# Import types
from type.response_type import ResponseType
from type.register_buy_type import RegisterBuyType
from type.register_sell_type import RegisterSellType

# Create the procedures router instance
procedures_controller: ProceduresController = ProceduresController()

# Create the procedures router
procedures_router: APIRouter = APIRouter(
    prefix="/api/procedures",
    tags=["Procedures"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to register a buy
@procedures_router.post("/register_buy", response_model=ResponseType)
async def register_buy(register_buy: RegisterBuyType):
    # Get the response
    response: ResponseType = procedures_controller.register_buy(register_buy)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to register a sell
@procedures_router.post("/register_sell", response_model=ResponseType)
async def register_sell(register_sell: RegisterSellType):
    # Get the response
    response: ResponseType = procedures_controller.register_sell(register_sell)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
