# Description: This file is used to create the product type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the product type class
class ProductType(BaseModel):
    pro_codigo: int | None = None
    pro_nombre: str
    pro_precio: float
    pro_descripcion: str
    pro_categoria: str


# Create the product type update class
class ProductTypeUpdate(BaseModel):
    pro_codigo: int
    pro_nombre: str | None = None
    pro_precio: float | None = None
    pro_descripcion: str | None = None
    pro_categoria: str | None = None
