# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.product_service import ProductService

# Importing types
from type.response_type import ResponseType
from type.product_type import ProductType, ProductTypeUpdate


# Create the product controller class
class ProductController:

    # Create constructor
    def __init__(self) -> None:
        self.product_service: ProductService = ProductService()

    # Create method to get all products
    def get_all_products(self) -> ResponseType[list[ProductType]]:
        # Return the response type
        return self.product_service.get_all_products()

    # Create method to get a product by id
    def get_product_by_id(self, product_id: int) -> ResponseType[ProductType]:
        # Return the response type
        return self.product_service.get_product_by_id(product_id)

    # Create method to create a product
    def create_product(self, product: ProductType) -> ResponseType:
        # Return the response type
        return self.product_service.create_product(product)

    # Create method to update a product
    def update_product(self, product: ProductTypeUpdate) -> ResponseType:
        # Return the response type
        return self.product_service.update_product(product)

    # Create method to delete a product
    def delete_product(self, product_id: int) -> ResponseType:
        # Return the response type
        return self.product_service.delete_product(product_id)