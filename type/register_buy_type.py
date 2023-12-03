# Description: This file is used to create the register buy type
# Author: Sebastian Gámez Ariza


# Importing libraries
from pydantic import BaseModel
from datetime import datetime


# Create the register buy type class
class RegisterBuyType(BaseModel):
    p_fecha: datetime
    p_cantidad: int
    p_precio: float
    p_total: float
    p_prv_nit: int
    p_pro_codigo: int
