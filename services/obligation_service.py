# Description: This file handles the database connection related with the obligation
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine

# Importing types
from type.response_type import ResponseType
from type.obligation_type import ObligationType, ObligationTypeUpdate


# Create the obligation services class
class ObligationService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all obligation
    def get_all_obligation(self) -> ResponseType[list[ObligationType]]:
        # Create the response type
        response_type: ResponseType[list[ObligationType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from obligacion"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Obligation found successfully",
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

    # Create method to get an obligation by id
    def get_obligation_by_id(self, obl_id: int) -> ResponseType[ObligationType]:
        # Create the response type
        response_type: ResponseType[ObligationType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                obligation, *_ = conn.execute(text("select * from obligacion where obl_id = :id"), {"id": obl_id})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Obligation found successfully",
                    data={
                        "obl_id": obligation.obl_id,
                        "obl_nombre": obligation.obl_nombre,
                        "obl_descripcion": obligation.obl_descripcion,
                        "obl_importe": obligation.obl_importe,
                        "obl_fecha_inicio": obligation.obl_fecha_inicio,
                        "obl_fecha_fin": obligation.obl_fecha_fin,
                        "emp_id": obligation.emp_id
                    }
                )
                # Commit the changes
                conn.commit()
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

    # Create a method to create an obligation
    def create_obligation(self, obligation: ObligationType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("insert into obligacion (obl_nombre, obl_descripcion, obl_importe, obl_fecha_inicio, obl_fecha_fin, emp_id) values (:obl_nombre, :obl_descripcion, :obl_importe, :obl_fecha_inicio, :obl_fecha_fin, :emp_id)"), {
                    "obl_nombre": obligation.obl_nombre,
                    "obl_descripcion": obligation.obl_descripcion,
                    "obl_importe": obligation.obl_importe,
                    "obl_fecha_inicio": obligation.obl_fecha_inicio,
                    "obl_fecha_fin": obligation.obl_fecha_fin,
                    "emp_id": obligation.emp_id
                })
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Obligation created successfully"
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

    # Create a method to update an obligation
    def update_obligation(self, obligation: ObligationTypeUpdate) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                for obligation_key, obligation_value in dict(obligation).items():
                    if obligation_value is not None and obligation_key != "obl_id":
                        # Execute the query
                        conn.execute(text(f"update obligacion set {obligation_key} = :value where obl_id = :id"), {
                            "value": obligation_value,
                            "id": obligation.obl_id
                        })
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Obligation updated successfully"
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

    # Create a method to delete an obligation
    def delete_obligation(self, obl_id: int) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("delete from obligacion where obl_id = :id"), {"id": obl_id})
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Obligation deleted successfully"
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
