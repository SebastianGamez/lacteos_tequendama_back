# Description: This file handles the database connection related with the procedures
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.register_buy_type import RegisterBuyType
from type.register_sell_type import RegisterSellType


# Create the procedures services class
class ProceduresService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to register a buy
    def register_buy(self, register_buy: RegisterBuyType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("call registrar_compra(:fecha, :cantidad, :precio, :total, :nit, :codigo)"),
                             {
                                 "fecha": register_buy.p_fecha,
                                 "cantidad": register_buy.p_cantidad,
                                 "precio": register_buy.p_precio,
                                 "total": register_buy.p_total,
                                 "nit": register_buy.p_prv_nit,
                                 "codigo": register_buy.p_pro_codigo
                             })
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Buy registered successfully"
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

    # Create method to register a sell
    def register_sell(self, register_sell: RegisterSellType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("call registrar_venta(:fecha, :total, :cliente, :empleado, :codigo)"),
                             {
                                 "fecha": register_sell.p_fecha,
                                 "total": register_sell.p_total,
                                 "cliente": register_sell.p_cli_id,
                                 "empleado": register_sell.p_emp_id,
                                 "codigo": register_sell.p_pro_codigo
                             })
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Sell registered successfully"
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
