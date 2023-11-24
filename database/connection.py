# Description: This file is used to create a connection to the database
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv('.env')

# Creating connection to the database
engine = create_engine(os.getenv('DATABASE_URL'))
