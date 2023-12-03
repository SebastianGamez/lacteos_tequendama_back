# Description: This file is used to create the sell detail view type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel
from datetime import datetime


# Create the sell detail view type class
class SellDetailViewType(BaseModel):
    fac_codigo: int
    fac_fecha: datetime
    cli_nombre: str
    emp_nombre: str
    pro_nombre: str
    pro_precio: int
