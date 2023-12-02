# Description: This file is used to create the empleado type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the empleado type class
class EmployeeType(BaseModel):
    emp_id: int | None = None
    emp_nombre: str
    emp_apellido: str
    emp_telefono: str
    emp_direccion: str
    emp_correo: str
    emp_cargo: str


class EmployeeTypeUpdate(BaseModel):
    emp_id: int
    emp_nombre: str | None = None
    emp_apellido: str | None = None
    emp_telefono: str | None = None
    emp_direccion: str | None = None
    emp_correo: str | None = None
    emp_cargo: str | None = None
