# Description: This file is used to create a connection to the database
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
