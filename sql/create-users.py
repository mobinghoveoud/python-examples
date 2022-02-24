import psycopg2
from psycopg2 import Error
from faker import Faker

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

    # Create users table in database
    query = '''CREATE TABLE users
              (user_id SERIAL primary key,
              name varchar(100),
              email varchar (150),
              phone_number varchar(50),
              age smallint);'''
    cursor.execute(query)
    connection.commit()

    # add fake user (1000)
    fake = Faker()

    for i in range(1000):
        insert_query = """INSERT INTO users (name, email, phone_number,age) VALUES (%s, %s, %s, %s)"""
        cursor.execute(insert_query, [fake.name(), fake.email(), fake.phone_number(), fake.random.randrange(1, 110)])
        connection.commit()


except (Exception, Error) as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
