# Description: This file contains the routes for the product.
# Author: Sebastián Gámez Ariza


# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.product_controller import ProductController

# Import types
from type.response_type import ResponseType
from type.product_type import ProductType, ProductTypeUpdate

# Create the product controller instance
product_controller: ProductController = ProductController()

# Create the product router
product_router: APIRouter = APIRouter(
    prefix="/api/product",
    tags=["Product"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to get all products
@product_router.get("/", response_model=ResponseType[list[ProductType]])
async def get_all_products():
    # Get the response
    response: ResponseType[list[ProductType]] = product_controller.get_all_products()
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to get a product by id
@product_router.get("/{product_id}", response_model=ResponseType[ProductType])
async def get_product_by_id(product_id: int) -> ResponseType[ProductType]:
    # Get the response
    response: ResponseType[ProductType] = product_controller.get_product_by_id(product_id)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to create a product
@product_router.post("/", response_model=ResponseType)
async def create_product(product: ProductType) -> ResponseType:
    # Get the response
    response: ResponseType = product_controller.create_product(product)
    # Check if the status is 200
    if response.status != 200:
        raise HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to update a product
@product_router.put("/", response_model=ResponseType)
async def update_product(product: ProductTypeUpdate) -> ResponseType:
    # Get the response
    response: ResponseType = product_controller.update_product(product)
    # Check if the status is 200
    if response.status != 200:
        HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response


# Create the route to delete a product
@product_router.delete("/{product_id}", response_model=ResponseType)
async def delete_product(product_id: int) -> ResponseType:
    # Get the response
    response: ResponseType = product_controller.delete_product(product_id)
    # Check if the status is 200
    if response.status != 200:
        HTTPException(status_code=response.status, detail=response.message)
    # Return the data
    return response
