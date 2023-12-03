# Description: This file handles the database connection related with the provider
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.provider_type import ProviderType, ProviderTypeUpdate


# Create the provider services class
class ProviderService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all providers
    def get_all_providers(self) -> ResponseType[list[ProviderType]]:
        # Create the response type
        response_type: ResponseType[list[ProviderType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from proveedor"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Providers found successfully",
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

    # Create method to get a provider by id
    def get_provider_by_id(self, prv_nit: int) -> ResponseType[ProviderType]:
        # Create the response type
        response_type: ResponseType[ProviderType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                provider, *_ = conn.execute(text("select * from proveedor where prv_nit = :nit"), {"nit": prv_nit})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Provider found successfully",
                    data=provider
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

    # Create method to create a provider
    def create_provider(self, provider: ProviderType) -> ResponseType[ProviderType]:
        # Create the response type
        response_type: ResponseType[ProviderType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("insert into proveedor values (:nit, :razon_social)"), {
                    "nit": provider.prv_nit,
                    "razon_social": provider.razon_social
                })
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Provider created successfully",
                    data=provider
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

    # Create method to update a provider
    def update_provider(self, provider: ProviderTypeUpdate) -> ResponseType[ProviderType]:
        # Create the response type
        response_type: ResponseType[ProviderType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("update proveedor set razon_social = :razon_social where prv_nit = :nit"), {
                    "nit": provider.prv_nit,
                    "razon_social": provider.razon_social
                })
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Provider updated successfully",
                    data=provider
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

    # Create method to delete a provider
    def delete_provider(self, prv_nit: int) -> ResponseType[ProviderType]:
        # Create the response type
        response_type: ResponseType[ProviderType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("delete from proveedor where prv_nit = :nit"), {"nit": prv_nit})
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Provider deleted successfully"
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
