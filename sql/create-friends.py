import psycopg2
from psycopg2 import Error
import random

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

    # Create friends table in database
    query = """CREATE TABLE friends
              (friend_id SERIAL primary key,
              user_id_1 int REFERENCES users(user_id),
              user_id_2 int REFERENCES users(user_id));"""
    cursor.execute(query)
    connection.commit()

    # Add some relation between users
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()

    for i in range(20):
        random_user = random.choices(users, k=2)
        query = "INSERT INTO friends (user_id_1, user_id_2) VALUES (%s, %s)"
        cursor.execute(query, [random_user[0], random_user[1]])
        connection.commit()

except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
