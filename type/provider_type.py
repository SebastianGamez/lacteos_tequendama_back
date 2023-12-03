# Description: This file is used to create the provider type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the provider type class
class ProviderType(BaseModel):
    prv_nit: int | None = None
    razon_social: str


# Create the provider type update class
class ProviderTypeUpdate(BaseModel):
    prv_nit: int
    razon_social: str | None = None