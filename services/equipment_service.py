# Description: This file handles the database connection related with the equipment
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.equipment_type import EquipmentType, EquipmentTypeUpdate


# Create the equipment type service class
class EquipmentService:
    # Create constructor
    def __init__(self) -> None:
        self.engine = engine

    # Create method to get all equipment types
    def get_all_equipment(self) -> ResponseType[list[EquipmentType]]:
        response_type: ResponseType[list[EquipmentType]]
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text("select * from equipamiento"))
                response_type = ResponseType(
                    status=200,
                    message="Equipments found successfully",
                    data=result.all()
                )
        except Exception as e:
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            print(e)

        return response_type

    # Create method to get an equipment type by id
    def get_equipment_by_id(self, equ_id: int) -> ResponseType[EquipmentType]:
        response_type: ResponseType[EquipmentType]
        try:
            with self.engine.connect() as conn:
                equipment_type, *_ = conn.execute(text("select * from equipamiento WHERE equ_id = :id"), {"id": equ_id})
                response_type = ResponseType(
                    status=200,
                    message="Equipment found successfully",
                    data={
                        'equ_id': equipment_type.equ_id,
                        'equ_nombre': equipment_type.equ_nombre,
                        'equ_categoria': equipment_type.equ_categoria
                    }
                )
        except Exception as e:
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            print(e)

        return response_type

    # Create method to create an equipment type
    def create_equipment(self, equipment: EquipmentType) -> ResponseType:
        response_type: ResponseType
        try:
            with self.engine.connect() as conn:
                conn.execute(
                    text("insert into equipamiento (equ_nombre, equ_categoria) values (:equ_nombre, :equ_categoria)"),
                    {
                        "equ_nombre": equipment.equ_nombre,
                        "equ_categoria": equipment.equ_categoria
                    }
                )
                response_type = ResponseType(
                    status=200,
                    message="Equipment created successfully",
                )
                conn.commit()
        except Exception as e:
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            print(e)

        return response_type

    # Create a method to update the equipment type
    def update_equipment(self, equipment: EquipmentTypeUpdate) -> ResponseType:
        response_type: ResponseType[EquipmentType]
        try:
            with self.engine.connect() as conn:
                for equipment_key, equipment_value in dict(equipment).items():
                    if equipment_value is not None and equipment_key != "equ_id":
                        conn.execute(
                            text(f"update equipamiento set {equipment_key} = :{equipment_key} where equ_id = :equ_id"),
                            {
                                equipment_key: equipment_value,
                                "equ_id": equipment.equ_id
                            }
                        )
                conn.commit()
                response_type = ResponseType(
                    status=200,
                    message="Equipment updated successfully",
                )
        except Exception as e:
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            print(e)

        return response_type

    # Create a method to delete the equipment type
    def delete_equipment(self, equ_id: int) -> ResponseType:
        response_type: ResponseType[EquipmentType]
        try:
            with self.engine.connect() as conn:
                conn.execute(
                    text("delete from equipamiento where equ_id = :equ_id"),
                    {
                        "equ_id": equ_id
                    }
                )
                response_type = ResponseType(
                    status=200,
                    message="Equipment deleted successfully",
                )
                conn.commit()
        except Exception as e:
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            print(e)

        return response_type
