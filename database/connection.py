# Description: This file is used to create a connection to the database
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy import create_engine
from config.env_variables_config import DATABASE_URL

# Creating connection to the database
engine = create_engine(DATABASE_URL)
