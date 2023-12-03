# Description: This file contains the routes for the obligation.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.obligation_controller import ObligationController

# Import types
from type.response_type import ResponseType
from type.obligation_type import ObligationType, ObligationTypeUpdate

# Create the obligation router instance
obligation_controller: ObligationController = ObligationController()

# Create the obligation router
obligation_router: APIRouter = APIRouter(
    prefix="/api/obligation",
    tags=["Obligation"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all obligations
@obligation_router.get("/", response_model=ResponseType[list[ObligationType]])
async def get_all_obligations():
    # Get the response
    response: ResponseType[list[ObligationType]] = obligation_controller.get_all_obligation()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get an obligation by id
@obligation_router.get("/{obl_id}", response_model=ResponseType[ObligationType])
async def get_obligation_by_id(obl_id: int):
    # Get the response
    response: ResponseType[ObligationType] = obligation_controller.get_obligation_by_id(obl_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create an obligation
@obligation_router.post("/", response_model=ResponseType)
async def create_obligation(obligation: ObligationType):
    # Get the response
    response: ResponseType = obligation_controller.create_obligation(obligation)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update an obligation
@obligation_router.put("/", response_model=ResponseType)
async def update_obligation(obligation: ObligationTypeUpdate):
    # Get the response
    response: ResponseType = obligation_controller.update_obligation(obligation)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response

# Create the route to delete an obligation
@obligation_router.delete("/{obl_id}", response_model=ResponseType)
async def delete_obligation(obl_id: int):
    # Get the response
    response: ResponseType = obligation_controller.delete_obligation(obl_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)

    # Return the data
    return response
