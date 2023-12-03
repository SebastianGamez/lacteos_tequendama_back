# Description: This file contains the routes for the sell detail view.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.sell_detail_view_controller import SellDetailViewController

# Import types
from type.response_type import ResponseType
from type.sell_detail_view_type import SellDetailViewType

# Create the sell detail view router instance
sell_detail_view_controller: SellDetailViewController = SellDetailViewController()

# Create the sell detail view router
sell_detail_view_router: APIRouter = APIRouter(
    prefix="/api/sell_detail_view",
    tags=["Sell Detail View"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all sell detail views
@sell_detail_view_router.get("/", response_model=ResponseType[list[SellDetailViewType]])
async def get_all_sell_detail_views():
    # Get the response
    response: ResponseType[list[SellDetailViewType]] = sell_detail_view_controller.get_all_sell_detail_view()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a sell detail view client name (cli_nombre)
@sell_detail_view_router.get("/client_name/{cli_nombre}", response_model=ResponseType[list[SellDetailViewType]])
async def get_sell_detail_view_by_client_name(cli_nombre: str):
    # Get the response
    response: ResponseType[list[SellDetailViewType]] = sell_detail_view_controller.get_all_sell_detail_view_by_client_name(cli_nombre)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a sell detail view by fac code (fac_codigo)
@sell_detail_view_router.get("/fac_code/{fac_codigo}", response_model=ResponseType[list[SellDetailViewType]])
async def get_sell_detail_view_by_fac_code(fac_codigo: int):
    # Get the response
    response: ResponseType[list[SellDetailViewType]] = sell_detail_view_controller.get_all_sell_detail_view_by_fac_code(fac_codigo)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
