# Description: This file contains the routes for the client.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.client_controller import ClientController

# Import types
from type.response_type import ResponseType
from type.client_type import ClientType, ClientTypeUpdate

# Create the client router instance
client_controller: ClientController = ClientController()

# Create the client router
client_router: APIRouter = APIRouter(
    prefix="/api/client",
    tags=["Client"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all clients
@client_router.get("/", response_model=ResponseType[list[ClientType]])
async def get_all_clients():
    # Get the response
    response: ResponseType[list[ClientType]] = client_controller.get_all_clients()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a client by id
@client_router.get("/{cli_id}", response_model=ResponseType[ClientType])
async def get_client_by_id(cli_id: int):
    # Get the response
    response: ResponseType[ClientType] = client_controller.get_client_by_id(cli_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create a client
@client_router.post("/", response_model=ResponseType)
async def create_client(client: ClientType):
    # Get the response
    response: ResponseType = client_controller.create_client(client)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update a client
@client_router.put("/", response_model=ResponseType)
async def update_client(client: ClientTypeUpdate):
    # Get the response
    response: ResponseType = client_controller.update_client(client)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete a client
@client_router.delete("/{cli_id}", response_model=ResponseType)
async def delete_client(cli_id: int):
    # Get the response
    response: ResponseType = client_controller.delete_client(cli_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
