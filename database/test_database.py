# Description: Test the database connection
# Author: Sebastián Gámez Ariza

# Importing libraries
from sqlalchemy import text, create_engine


# Create the test to validate the database connection
def test_database_connection(egn: create_engine):
    with egn.connect() as conn:
        # Execute the query
        result = conn.execute(text("select 'DATABASE CONNECTION SUCCESSFUL'"))
        # Print the result

        print(f'\n', f'{list(result.all())[0][0]}'.center(105, '-'), end='\n\n')
