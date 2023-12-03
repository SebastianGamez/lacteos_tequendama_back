# Description: This file contains the routes for the provider.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.provider_controller import ProviderController

# Import types
from type.response_type import ResponseType
from type.provider_type import ProviderType, ProviderTypeUpdate

# Create the provider router instance
provider_controller: ProviderController = ProviderController()

# Create the provider router
provider_router: APIRouter = APIRouter(
    prefix="/api/provider",
    tags=["Provider"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all providers
@provider_router.get("/", response_model=ResponseType[list[ProviderType]])
async def get_all_providers():
    # Get the response
    response: ResponseType[list[ProviderType]] = provider_controller.get_all_providers()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a provider by id
@provider_router.get("/{prv_nit}", response_model=ResponseType[ProviderType])
async def get_provider_by_id(prv_nit: int):
    # Get the response
    response: ResponseType[ProviderType] = provider_controller.get_provider_by_id(prv_nit)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create a provider
@provider_router.post("/", response_model=ResponseType)
async def create_provider(provider: ProviderType):
    # Get the response
    response: ResponseType = provider_controller.create_provider(provider)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update a provider
@provider_router.put("/", response_model=ResponseType)
async def update_provider(provider: ProviderTypeUpdate):
    # Get the response
    response: ResponseType = provider_controller.update_provider(provider)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete a provider
@provider_router.delete("/{prv_nit}", response_model=ResponseType)
async def delete_provider(prv_nit: int):
    # Get the response
    response: ResponseType = provider_controller.delete_provider(prv_nit)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
