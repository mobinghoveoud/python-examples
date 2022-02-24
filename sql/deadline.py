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

    # Show tasks sort by deadline
    cursor.execute("SELECT * FROM tasks ORDER BY deadline")
    tasks = cursor.fetchall()

    print("task_id    title    estimated_time    value    deadline    user_id")
    for task in tasks:
        print(task)

except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
