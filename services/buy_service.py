# Description: This file handles the database connection related with the buy
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.buy_type import BuyType, BuyTypeUpdate
from type.response_type import ResponseType


# Create the buy services class
class BuyService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all buys
    def get_all_buys(self) -> ResponseType[list[BuyType]]:
        # Create the response type
        response_type: ResponseType[list[BuyType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from compra"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Buys found successfully",
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

    # Create method to get a buy by id
    def get_buy_by_id(self, com_codigo: int) -> ResponseType[BuyType]:
        # Create the response type
        response_type: ResponseType[BuyType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                buy, *_ = conn.execute(text("select * from compra where com_codigo = :id"), {"id": com_codigo})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Buy found successfully",
                    data={
                        'com_codigo': buy.com_codigo,
                        'com_fecha': buy.com_fecha,
                        'com_cantidad': buy.com_cantidad,
                        'com_precio': buy.com_precio,
                        'com_total': buy.com_total,
                        'prv_nit': buy.prv_nit
                    }
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
            )

        # Return the response type
        return response_type

    # Create method to create a buy
    def create_buy(self, buy: BuyType) -> ResponseType:
        # Create the response type
        response_type: ResponseType[BuyType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(
                    text("insert into compra (com_fecha, com_cantidad, com_precio, com_total, prv_nit) values (:com_fecha, :com_cantidad, :com_precio, :com_total, :prv_nit)"),
                    {
                        "com_fecha": buy.com_fecha,
                        "com_cantidad": buy.com_cantidad,
                        "com_precio": buy.com_precio,
                        "com_total": buy.com_total,
                        "prv_nit": buy.prv_nit
                    }
                )
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Buy created successfully",
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
                data={}
            )

        # Return the response type
        return response_type

    # Create method to update a buy
    def update_buy(self, buy: BuyTypeUpdate) -> ResponseType:
        # Create the response type
        response_type: ResponseType[BuyType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                for buy_key, buy_value in dict(buy).items():
                    if buy_value is not None and buy_key != "com_codigo":
                        # Execute the query
                        conn.execute(
                            text(f"update compra set {buy_key} = :{buy_key} where com_codigo = :com_codigo"),
                            {
                                "com_codigo": buy.com_codigo,
                                buy_key: buy_value
                            }
                        )
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Buy updated successfully",
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
                data={}
            )

        # Return the response type
        return response_type

    # Create method to delete a buy
    def delete_buy(self, com_codigo: int) -> ResponseType:
        # Create the response type
        response_type: ResponseType[BuyType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("delete from compra where com_codigo = :com_codigo"), {"com_codigo": com_codigo})
                # Commit the transaction
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Buy deleted successfully",
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e),
            )

        # Return the response type
        return response_type
