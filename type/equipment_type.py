# Description: This file is used to create the equipment type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the equipment type class
class EquipmentType(BaseModel):
    equ_id: int | None = None
    equ_nombre: str
    equ_categoria: str


# Create the equipment type update class
class EquipmentTypeUpdate(BaseModel):
    equ_id: int
    equ_nombre: str | None = None
    equ_categoria: str | None = None