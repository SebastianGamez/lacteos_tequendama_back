# Description: This file contains the environment variables configuration
# Author: Sebastián Gámez Ariza

from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv('.env.dev')

# Set the env variables
DATABASE_URL: str = os.getenv('DATABASE_URL')
