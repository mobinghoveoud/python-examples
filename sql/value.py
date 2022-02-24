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

    # Sum all the values of a specific user_id
    cursor.execute("SELECT SUM(value) FROM tasks where user_id=%s",input("user id: "))
    sum = cursor.fetchone()
    print(sum[0])

except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
