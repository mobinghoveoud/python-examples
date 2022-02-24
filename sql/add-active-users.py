import psycopg2
from psycopg2 import Error

try:
    # Connection
    connection = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='mobin1234',
        host='localhost',
        port='5432'
    )
    cursor = connection.cursor()

    # Add column is_active with default value (true) in users table
    query = "ALTER TABLE users ADD is_active BOOLEAN  DEFAULT TRUE"
    cursor.execute(query)
    connection.commit()

except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
