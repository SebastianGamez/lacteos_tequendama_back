# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.provider_service import ProviderService

# Importing types
from type.response_type import ResponseType
from type.provider_type import ProviderType, ProviderTypeUpdate


# Create the provider controller class
class ProviderController:

    # Create constructor
    def __init__(self) -> None:
        self.provider_service: ProviderService = ProviderService()

    # Create method to get all providers
    def get_all_providers(self) -> ResponseType[list[ProviderType]]:
        # Return the response type
        return self.provider_service.get_all_providers()

    # Create method to get a provider by id
    def get_provider_by_id(self, prv_nit: int) -> ResponseType[ProviderType]:
        # Return the response type
        return self.provider_service.get_provider_by_id(prv_nit)

    # Create method to create a provider
    def create_provider(self, provider: ProviderType) -> ResponseType:
        # Return the response type
        return self.provider_service.create_provider(provider)

    # Create method to update a provider
    def update_provider(self, provider: ProviderTypeUpdate) -> ResponseType:
        # Return the response type
        return self.provider_service.update_provider(provider)

    # Create method to delete a provider
    def delete_provider(self, prv_nit: int) -> ResponseType:
        # Return the response type
        return self.provider_service.delete_provider(prv_nit)
