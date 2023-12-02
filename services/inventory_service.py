# Description: This file handles the database connection related with the inventory
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.inventory_type import InventoryType, InventoryTypeUpdate


# Create the inventory services class
class InventoryService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all inventory
    def get_all_inventory(self) -> ResponseType[list[InventoryType]]:
        # Create the response type
        response_type: ResponseType[list[InventoryType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from inventario"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Inventory found successfully",
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

    # Create method to get an inventory by id
    def get_inventory_by_id(self, inv_id: int) -> ResponseType[InventoryType]:
        # Create the response type
        response_type: ResponseType[InventoryType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                inventory, *_ = conn.execute(text("select * from inventario where inv_id = :id"), {"id": inv_id})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Inventory found successfully",
                    data={
                        "inv_id": inventory.inv_id,
                        "inv_nombre": inventory.inv_nombre,
                        "inv_cantidad": inventory.inv_cantidad,
                        "inv_categoria": inventory.inv_categoria,
                        "inv_fecha": inventory.inv_fecha,
                        "pro_codigo": inventory.pro_codigo
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

    # Create method to create an inventory
    def create_inventory(self, inventory: InventoryType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("insert into inventario (inv_nombre, inv_cantidad, inv_categoria, inv_fecha, pro_codigo) values (:inv_nombre, :inv_cantidad, :inv_categoria, :inv_fecha, :pro_codigo)"), {
                    "inv_nombre": inventory.inv_nombre,
                    "inv_cantidad": inventory.inv_cantidad,
                    "inv_categoria": inventory.inv_categoria,
                    "inv_fecha": inventory.inv_fecha,
                    "pro_codigo": inventory.pro_codigo
                })
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Inventory created successfully"
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

    # Create method to update an inventory
    def update_inventory(self, inventory: InventoryTypeUpdate) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                for inventory_key, inventory_value in dict(inventory).items():
                    if inventory_value is not None and inventory_key != "inv_id":
                        # Execute the query
                        conn.execute(text(f"update inventario set {inventory_key} = :value where inv_id = :id"), {
                            "value": inventory_value,
                            "id": inventory.inv_id
                        })
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Inventory updated successfully"
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

    # Create method to delete an inventory
    def delete_inventory(self, inv_id: int) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("delete from inventario where inv_id = :id"), {"id": inv_id})
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Inventory deleted successfully"
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


