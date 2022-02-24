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

    # Get friends of user that age > 18
    cursor.execute("SELECT user_id,name FROM users WHERE age > 18")
    users = cursor.fetchall()

    for user in users:
        cursor.execute("SELECT user_id_2 FROM friends WHERE user_id_1 = %s OR user_id_2 = %s", [user[0], user[0]])
        friends = cursor.fetchall()

        print("friends of", user[1], ":")
        for friend in friends:
            cursor.execute("SELECT name FROM users WHERE user_id = %s", [friend[0]])
            name = cursor.fetchone()[0]
            print(name, end=", ")
        print("\n")


except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
