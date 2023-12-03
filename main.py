# Description: Main file of the project
# Author: Sebastián Gámez Ariza

# Import FastAPI libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database connection
from database.connection import engine
from database.test_database import test_database_connection

# Import the routes
from routes.client_route import client_router
from routes.buy_route import buy_router
from routes.employee_route import employee_router
from routes.equipment_route import equipment_router
from routes.sell_route import sell_router
from routes.inventory_route import inventory_router
from routes.obligation_route import obligation_router
from routes.product_route import product_router
from routes.provider_route import provider_router
from routes.employee_equipment_view_route import employee_equipment_view_router

# Test the database connection
test_database_connection(engine)

# Create the app
app = FastAPI()

# Set cors
app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

# Include the routes
app.include_router(client_router)
app.include_router(buy_router)
app.include_router(employee_router)
app.include_router(equipment_router)
app.include_router(sell_router)
app.include_router(inventory_router)
app.include_router(obligation_router)
app.include_router(product_router)
app.include_router(provider_router)
app.include_router(employee_equipment_view_router)
