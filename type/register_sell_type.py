# Description: This file is used to create the register sell type
# Author: Sebastian Gámez Ariza


# Importing libraries
from pydantic import BaseModel
from datetime import datetime


# Create the register sell type class
class RegisterSellType(BaseModel):
    p_fecha: datetime
    p_total: float
    p_cli_id: int
    p_emp_id: int
    p_pro_codigo: int
