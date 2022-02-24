import psycopg2
from psycopg2 import Error
from faker import Faker
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

    # Create tasks table in database
    query = '''CREATE TABLE tasks
              (task_id SERIAL primary key,
              title varchar(200),
              estimated_time smallint,
              value smallint,
              deadline date,
              user_id int REFERENCES users(user_id));'''
    cursor.execute(query)
    connection.commit()

    # add fake task (20)
    fake = Faker()

    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()

    for i in range(20):
        insert_query = """INSERT INTO tasks 
        (title, estimated_time, value, deadline, user_id) 
        VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, [fake.word(), fake.random.randrange(1, 100), fake.random.randrange(1, 100),
                                      fake.date_time_between(start_date="now", end_date="+2y"),
                                      random.choice(users)])
        connection.commit()


except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
