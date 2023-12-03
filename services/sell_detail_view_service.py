# Description: This file handles the database connection related with the sell detail view
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.sell_detail_view_type import SellDetailViewType


# Create the sell detail view services class
class SellDetailViewService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all sell detail view
    def get_all_sell_detail_view(self) -> ResponseType[list[SellDetailViewType]]:
        # Create the response type
        response_type: ResponseType[list[SellDetailViewType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from vista_facturas_venta_detalladas"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell detail view found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to get a sell detail view fac code (fac_codigo)
    def get_sell_detail_view_fac_code(self, fac_codigo: int) -> ResponseType[list[SellDetailViewType]]:
        # Create the response type
        response_type: ResponseType[list[SellDetailViewType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from vista_facturas_venta_detalladas where fac_codigo = :id"), {"id": fac_codigo})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell detail view found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to get a sell detail view by client name (cli_nombre)
    def get_sell_detail_view_by_client_name(self, cli_nombre: str) -> ResponseType[list[SellDetailViewType]]:
        # Create the response type
        response_type: ResponseType[list[SellDetailViewType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from vista_facturas_venta_detalladas where cli_nombre = :name"), {"name": cli_nombre})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell detail view found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type
