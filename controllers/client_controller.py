# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.client_service import ClientService

# Importing types
from type.response_type import ResponseType
from type.client_type import ClientType, ClientTypeUpdate


# Create the client controller class
class ClientController:

    # Create constructor
    def __init__(self) -> None:
        self.client_service: ClientService = ClientService()

    # Create method to get all clients
    def get_all_clients(self) -> ResponseType[list[ClientType]]:
        # Return the response type
        return self.client_service.get_all_clients()

    # Create method to get a client by id
    def get_client_by_id(self, cli_id: int) -> ResponseType[ClientType]:
        # Return the response type
        return self.client_service.get_client_by_id(cli_id)
    
    # Create method to create a client
    def create_client(self, client: ClientType) -> ResponseType:
        # Return the response type
        return self.client_service.create_client(client)
    
    # Create method to update a client
    def update_client(self, client: ClientTypeUpdate) -> ResponseType:
        # Return the response type
        return self.client_service.update_client(client)
    
    # Create method to delete a client
    def delete_client(self, cli_id: int) -> ResponseType:
        # Return the response type
        return self.client_service.delete_client(cli_id)
