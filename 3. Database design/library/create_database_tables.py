import psycopg2

# To resolve the path for the config file
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from database_config import username, password, host, port
from populate_tables import test_data

def execute_commands(connection: psycopg2.connect, commands: list):
    connection.autocommit = True
    cursor = connection.cursor()

    for command in commands:
        cursor.execute(command)

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
    # TODO: The constraints throw an error, can't reference before constraint creation
    commands = ["""CREATE TABLE IF NOT EXISTS catalog (
        id SERIAL PRIMARY KEY,
        book_id INT,
        book_name VARCHAR(255) UNIQUE,
        publisher_id INT
    )""",
    """CREATE TABLE IF NOT EXISTS book (
        id SERIAL PRIMARY KEY,
        book_name VARCHAR(255) UNIQUE,
        publisher_id INT,
        copy_count INT
    ) """,
    """CREATE TABLE IF NOT EXISTS publisher (
        id SERIAL PRIMARY KEY,
        book_id INT,
        customer_id INT,
        loan_date DATE,
        due_date DATE
    )
    """,
    """CREATE TABLE IF NOT EXISTS loan (
        id SERIAL PRIMARY KEY,
        book_id INT,
        customer_id INT,
        loan_date DATE,
        due_date DATE
    )
    """,
    """CREATE TABLE IF NOT EXISTS customer (
        id SERIAL PRIMARY KEY,
        customer_name VARCHAR(255),
        address VARCHAR(255),
        email VARCHAR(255),
        phone_number VARCHAR(14)
    )
    """]

    execute_commands(connection, commands)

def add_constraints():
    connection = psycopg2.connect(
        host = host,
        database = "library",
        user = username,
        password = password,
        port = port
    )
    commands = ["""
        ALTER TABLE catalog
        ADD CONSTRAINT fk_catalog_bookname FOREIGN KEY (book_name) REFERENCES book(book_name),
        ADD CONSTRAINT fk_catalog_bookid FOREIGN KEY (book_id) REFERENCES book(id),
        ADD CONSTRAINT fk_catalog_publisherid FOREIGN KEY (publisher_id) REFERENCES publisher(id)
        """,
        """
        ALTER TABLE book
        ADD CONSTRAINT fk_book_publisherid FOREIGN KEY (publisher_id) REFERENCES publisher(id)
        """,
        """
        ALTER TABLE publisher
        ADD CONSTRAINT fk_publisher_bookid FOREIGN KEY (book_id) REFERENCES book(id),
        ADD CONSTRAINT fk_publisher_customerid FOREIGN KEY (customer_id) REFERENCES customer(id)
        """,
        """
        ALTER TABLE loan
        ADD CONSTRAINT fk_loan_bookid FOREIGN KEY (book_id) REFERENCES book(id),
        ADD CONSTRAINT fk_loan_customerid FOREIGN KEY (customer_id) REFERENCES customer(id)
        """]
    execute_commands(connection, commands)

def drop_database():
    connection = psycopg2.connect(
        host = host,
        database = "postgres",
        user = username,
        password = password,
        port = port
    )
    connection.autocommit = True
    connection.cursor().execute("DROP DATABASE library")

drop_database()
create_database()
create_tables()
test_data()
add_constraints()
