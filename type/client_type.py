# Description: This file is used to create the client type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the client type class
class ClientType(BaseModel):
    cli_id: int | None = None
    cli_nombre: str


# Create the client type update class
class ClientTypeUpdate(BaseModel):
    cli_id: int
    cli_nombre: str | None = None
