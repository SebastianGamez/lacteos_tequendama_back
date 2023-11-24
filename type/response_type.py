# Description: This file is used to create a response type
# Author: Sebastian Gámez Ariza


# Importing libraries
from pydantic import BaseModel
from typing import Generic, TypeVar

# Create the generic type
T = TypeVar('T')


# Create the response type class
class ResponseType(BaseModel, Generic[T]):
    status: int
    message: str
    data: T | None = None
