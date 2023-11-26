# Description: Main file of the project
# Author: Sebastián Gámez Ariza

# Import FastAPI libraries
from fastapi import FastAPI

# Import database connection
from database.connection import engine
from database.test_database import test_database_connection

# Import the routes
from routes.client_route import client_router
from routes.buy_route import buy_router

# Test the database connection
test_database_connection(engine)

# Create the app
app = FastAPI()

# Include the routes
app.include_router(client_router)
app.include_router(buy_router)

