# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.obligation_service import ObligationService

# Importing types
from type.response_type import ResponseType
from type.obligation_type import ObligationType, ObligationTypeUpdate


# Create the obligation controller class
class ObligationController:

    # Create constructor
    def __init__(self) -> None:
        self.obligation_service: ObligationService = ObligationService()

    # Create method to get all obligation
    def get_all_obligation(self) -> ResponseType[list[ObligationType]]:
        # Return the response type
        return self.obligation_service.get_all_obligation()

    # Create method to get an obligation by id
    def get_obligation_by_id(self, obl_id: int) -> ResponseType[ObligationType]:
        # Return the response type
        return self.obligation_service.get_obligation_by_id(obl_id)

    # Create method to create an obligation
    def create_obligation(self, obligation: ObligationType) -> ResponseType:
        # Return the response type
        return self.obligation_service.create_obligation(obligation)

    # Create method to update an obligation
    def update_obligation(self, obligation: ObligationTypeUpdate) -> ResponseType:
        # Return the response type
        return self.obligation_service.update_obligation(obligation)

    # Create method to delete an obligation
    def delete_obligation(self, obl_id: int) -> ResponseType:
        # Return the response type
        return self.obligation_service.delete_obligation(obl_id)
