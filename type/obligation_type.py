# Description: This file is used to create the obligation type
# Author: Sebastian Gámez Ariza


# Importing libraries
from pydantic import BaseModel
from datetime import datetime


# Create the obligation type class
class ObligationType(BaseModel):
    obl_id: int | None = None
    obl_nombre: str
    obl_descripcion: str
    obl_importe: int
    obl_fecha_inicio: datetime
    obl_fecha_fin: datetime
    emp_id: int


# Create the obligation type update class
class ObligationTypeUpdate(BaseModel):
    obl_id: int
    obl_nombre: str | None = None
    obl_descripcion: str | None = None
    obl_importe: int | None = None
    obl_fecha_inicio: datetime | None = None
    obl_fecha_fin: datetime | None = None
    emp_id: int | None = None
