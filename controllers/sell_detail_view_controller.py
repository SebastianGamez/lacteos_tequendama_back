# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.sell_detail_view_service import SellDetailViewService

# Importing types
from type.response_type import ResponseType
from type.sell_detail_view_type import SellDetailViewType


# Create the sell detail view controller class
class SellDetailViewController:

    # Create constructor
    def __init__(self) -> None:
        self.sell_detail_view_service: SellDetailViewService = SellDetailViewService()

    # Create method to get all sell detail view
    def get_all_sell_detail_view(self) -> ResponseType[list[SellDetailViewType]]:
        # Return the response type
        return self.sell_detail_view_service.get_all_sell_detail_view()

    # Create method to get all sell detail view by fac code (fac_codigo)
    def get_all_sell_detail_view_by_fac_code(self, fac_codigo: int) -> ResponseType[list[SellDetailViewType]]:
        # Return the response type
        return self.sell_detail_view_service.get_sell_detail_view_fac_code(fac_codigo)

    # Create method to get all sell detail view by client name (cli_nombre)
    def get_all_sell_detail_view_by_client_name(self, cli_nombre: str) -> ResponseType[list[SellDetailViewType]]:
        # Return the response type
        return self.sell_detail_view_service.get_sell_detail_view_by_client_name(cli_nombre)
