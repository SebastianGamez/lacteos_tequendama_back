# Description: This file handles the database connection related with the client
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.client_type import ClientType, ClientTypeUpdate
from type.response_type import ResponseType


# Create the client services class
class ClientService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all clients
    def get_all_clients(self) -> ResponseType[list[ClientType]]:
        # Create the response type
        response_type: ResponseType[list[ClientType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from cliente"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Clients found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
                data=[]
            )

        # Return the response type
        return response_type

    # Create method to get a client by id
    def get_client_by_id(self, cli_id: int) -> ResponseType[ClientType]:
        # Create the response type
        response_type: ResponseType[ClientType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                client, *_ = conn.execute(text("select * from cliente where cli_id = :id"), {"id": cli_id})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Client found successfully",
                    data={
                        'cli_id': client.cli_id,
                        'cli_nombre': client.cli_nombre
                    }
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
                data=[]
            )

        # Return the response type
        return response_type

    # Create method to create a client
    def create_client(self, client: ClientType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(
                    text("insert into cliente (cli_nombre) values (:cli_nombre)"),
                    {
                        "cli_nombre": client.cli_nombre
                    }
                )
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Client created successfully",
                )
                conn.commit()
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
            )

        # Return the response type
        return response_type

    # Create a method to update the client
    def update_client(self, client: ClientTypeUpdate) -> ResponseType:
        # Create the response type
        response_type: ResponseType[ClientType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                for client_key, client_value in dict(client).items():
                    if client_value is not None and client_key != "cli_id":
                        # Execute the query
                        conn.execute(
                            text(f"update cliente set {client_key} = :{client_key} where cli_id = :cli_id"),
                            {
                                client_key: client_value,
                                "cli_id": client.cli_id
                            }
                        )
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Client updated successfully",
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
            )

        # Return the response type
        return response_type

    # Create a method to delete the client
    def delete_client(self, cli_id: int) -> ResponseType:
        # Create the response type
        response_type: ResponseType[ClientType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(
                    text("delete from cliente where cli_id = :cli_id"),
                    {
                        "cli_id": cli_id
                    }
                )
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Client deleted successfully",
                )
                conn.commit()
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
            )

        # Return the response type
        return response_type
