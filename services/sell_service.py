# Description: This file handles the database connection related with the sell
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.sell_type import SellType, SellTypeUpdate


# Create the sell services class
class SellService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all sells
    def get_all_sells(self) -> ResponseType[list[SellType]]:
        # Create the response type
        response_type: ResponseType[list[SellType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from factura_venta"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sells found successfully",
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

    # Create method to get a sell by id
    def get_sell_by_id(self, fac_codigo: int) -> ResponseType[SellType]:
        # Create the response type
        response_type: ResponseType[SellType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                sell, *_ = conn.execute(text("select * from factura_venta where fac_codigo = :id"), {"id": fac_codigo})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell found successfully",
                    data={
                        "fac_codigo": sell.fac_codigo,
                        "fac_fecha": sell.fac_fecha,
                        "fac_total": sell.fac_total,
                        "cli_id": sell.cli_id,
                        "emp_id": sell.emp_id
                    }
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

    # Create method to create a sell
    def create_sell(self, sell: SellType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(
                    text(
                        "insert into factura_venta (fac_fecha, fac_total, cli_id, emp_id) values (:fac_fecha, :fac_total, :cli_id, :emp_id)"),
                    {
                        "fac_fecha": sell.fac_fecha,
                        "fac_total": sell.fac_total,
                        "cli_id": sell.cli_id,
                        "emp_id": sell.emp_id
                    }
                )
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell created successfully"
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

    # Create method to update a sell
    def update_sell(self, sell: SellTypeUpdate) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                for sell_key, sell_value in dict(sell).items():
                    if sell_value is not None and sell_key != "fac_codigo":
                        # Execute the query
                        conn.execute(
                            text(f"update factura_venta set {sell_key} = :{sell_key} where fac_codigo = :fac_codigo"),
                            {
                                "fac_codigo": sell.fac_codigo,
                                sell_key: sell_value
                            }
                        )
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell updated successfully"
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

    # Create method to delete a sell
    def delete_sell(self, fac_codigo: int) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("delete from factura_venta where fac_codigo = :fac_codigo"), {"fac_codigo": fac_codigo})
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell deleted successfully"
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
