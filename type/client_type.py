# Description: This file is used to create the client type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the client type class
class ClientType(BaseModel):
    cli_id: int | None = None
    cli_nombre: str
