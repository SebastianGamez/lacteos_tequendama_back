# Description: This file handles the database connection related with the product
# Author: Sebastian Gámez Ariza


# Importing libraries
from sqlalchemy import text, create_engine
from database.connection import engine


# Importing types
from type.product_type import ProductType, ProductTypeUpdate
from type.response_type import ResponseType


# Create the product services class
class ProductService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: create_engine = engine

    # Create method to get all products
    def get_all_products(self) -> ResponseType[list[ProductType]]:
        # Create the response type
        response_type: ResponseType[list[ProductType]]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                result = conn.execute(text("select * from producto"))
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Products found successfully",
                    data=result.all()
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to get a product by id
    def get_product_by_id(self, pro_codigo: int) -> ResponseType[ProductType]:
        # Create the response type
        response_type: ResponseType[ProductType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                product, *_ = conn.execute(text("select * from producto where pro_codigo = :id"), {"id": pro_codigo})
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Product found successfully",
                    data=product
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to create a product
    def create_product(self, product: ProductType) -> ResponseType:
        # Create the response type
        response_type: ResponseType[ProductType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(
                    text("insert into producto (pro_nombre, pro_precio, pro_descripcion, pro_categoria) values (:pro_nombre, :pro_precio, :pro_descripcion, :pro_categoria)"),
                    {
                        "pro_nombre": product.pro_nombre,
                        "pro_precio": product.pro_precio,
                        "pro_descripcion": product.pro_descripcion,
                        "pro_categoria": product.pro_categoria
                    }
                )
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Product created successfully",
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to update a product
    def update_product(self, product: ProductTypeUpdate) -> ResponseType:
        # Create the response type
        response_type: ResponseType[ProductTypeUpdate]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                for product_key, product_value in dict(product).items():
                    if product_key != 'pro_codigo' and product_value is not None:
                        conn.execute(
                            text(f"update producto set {product_key} = :{product_key} where pro_codigo = :pro_codigo"),
                            {
                                product_key: product_value,
                                "pro_codigo": product.pro_codigo
                            }
                        )
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Product updated successfully",
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type

    # Create method to delete a product
    def delete_product(self, pro_codigo: int) -> ResponseType:
        # Create the response type
        response_type: ResponseType[ProductType]
        try:
            # Create the connection
            with self.engine.connect() as conn:
                # Execute the query
                conn.execute(text("delete from producto where pro_codigo = :id"), {"id": pro_codigo})
                # Commit the changes
                conn.commit()
                # Create the response type
                response_type = ResponseType(
                    status=200,
                    message="Product deleted successfully"
                )
        except Exception as e:
            # Create the response type
            response_type = ResponseType(
                status=500,
                message=str(e)
            )
            # Log the error
            print(e)

        # Return the response type
        return response_type
