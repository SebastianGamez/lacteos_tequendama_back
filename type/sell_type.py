# Description: This file is used to create the sell type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel
from datetime import datetime


# Create the sell type class
class SellType(BaseModel):
    fac_codigo: int | None = None
    fac_fecha: datetime
    fac_total: float
    cli_id: int
    emp_id: int


# Create the sell type update class
class SellTypeUpdate(BaseModel):
    fac_codigo: int
    fac_fecha: datetime | None = None
    fac_total: float | None = None
    cli_id: int | None = None
    emp_id: int | None = None
