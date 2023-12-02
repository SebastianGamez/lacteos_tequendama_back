# Description: This file is used to create the inventory type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel
from datetime import datetime


# Create the inventory type class
class InventoryType(BaseModel):
    inv_id: int | None = None
    inv_nombre: str
    inv_cantidad: int
    inv_categoria: str
    inv_fecha: datetime
    pro_codigo: int


# Create the inventory type update class
class InventoryTypeUpdate(BaseModel):
    inv_id: int
    inv_nombre: str | None = None
    inv_cantidad: int | None = None
    inv_categoria: str | None = None
    inv_fecha: datetime | None = None
    pro_codigo: int | None = None