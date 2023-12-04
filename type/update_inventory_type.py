# Description: This file is used to create the update inventory type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel

# Create the update inventory type class

class UpdateInventoryType(BaseModel):
    p_pro_codigo: int
    p_cantidad: int
