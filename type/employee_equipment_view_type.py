# Description: This file is used to create the employee with equipment type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the employee with equipment type class
class EmployeeEquipmentViewType(BaseModel):
    emp_id: int
    emp_nombre: str
    emp_apellido: str
    emp_cargo: str
    equ_id: int
    equ_nombre: str


# Create the employee with equipment type update class
class EmployeeEquipmentViewTypeUpdate(BaseModel):
    emp_id: int
    emp_nombre: str | None = None
    emp_apellido: str | None = None
    emp_cargo: str | None = None
    equ_id: int | None = None
    equ_nombre: str | None = None
