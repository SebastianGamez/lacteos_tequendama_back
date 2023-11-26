# Description: This file is used to create the buy type
# Author: Sebastian Gámez Ariza
import datetime

# Importing libraries
from pydantic import BaseModel


# Create the buy type class
class BuyType(BaseModel):
    com_codigo: int | None = None
    com_fecha: datetime.date
    com_cantidad: int
    com_precio: float
    com_total: float
    prv_nit: int


# Create the buy type update class
class BuyTypeUpdate(BaseModel):
    com_codigo: int
    com_fecha: datetime.date | None = None
    com_cantidad: int | None = None
    com_precio: float | None = None
    com_total: float | None = None
    prv_nit: int | None = None
