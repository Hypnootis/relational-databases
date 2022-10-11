import psycopg2

# To resolve the path for the config file
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from database_config import username, password, host, port

def execute_commands(connection: psycopg2.connect, commands: list):
    connection.autocommit = True
    cursor = connection.cursor()

    for command in commands:
        cursor.execute(commands)

    connection.close()

def create_database():
    connection = psycopg2.connect(
        host = host,
        database = "postgres",
        user = username,
        password = password,
        port = port
    )
    commands = ["CREATE DATABASE library"]

    try:
        execute_commands(connection, commands)
    except:
        print("Connection must be a psycopg2.connect() type!")

def create_tables():
    connection = psycopg2.connect(
        host = host,
        database = "library",
        user = username,
        password = password,
        port = port
    )
    commands = ["""CREATE TABLE IF NOT EXISTS catalog (
        id SERIAL PRIMARY KEY,
        book_ID INT REFERENCES book(id),
        book_name VARCHAR(255) REFERENCES book(book_name),
        publisher_id INT REFERENCES publisher(id)
    )""",
    """CREATE TABLE IF NOT EXISTS book (
        id SERIAL PRIMARY KEY,
        book_name VARCHAR(255),
        publisher_id int REFERENCES publisher(id),
        copy_count INT
    ) """,
    """CREATE TABLE IF NOT EXISTS publisher (
        id SERIAL PRIMARY KEY,
        book_id INT REFERENCES book(id),
        customer_id INT REFERENCES customer(id),
        loan_date DATE,
        due_date DATE
    )
    """]
    execute_commands(connection, commands)

create_database()
create_tables()
