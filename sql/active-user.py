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

    # Update active_user (age < 18)
    query = "UPDATE users set is_active=FALSE where age < 18"
    cursor.execute(query)
    connection.commit()

except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
