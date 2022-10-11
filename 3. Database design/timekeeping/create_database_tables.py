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
    commands = ["CREATE DATABASE timekeeping"]

    try:
        execute_commands(connection, commands)
    except:
        print("Connection must be a psycopg2.connect() type!")

def create_tables():
    connection = psycopg2.connect(
        host = host,
        database = "timekeeping",
        user = username,
        password = password,
        port = port
    )
    commands = ["""CREATE TABLE IF NOT EXISTS employee (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )""",
    """CREATE TABLE IF NOT EXISTS project (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255)
    ) """,
    """CREATE TABLE IF NOT EXISTS timetable (
        id SERIAL PRIMARY KEY,
        id SERIAL PRIMARY KEY,
        entry_date DATE,
        project_id INT REFERENCES project(id),
        project_name VARCHAR(255) REFERENCES project(name),
        employee_id INT REFERENCES employee(id),
        employee_name VARCHAR(255) REFERENCES employee(name),
        hours_worked INT
    )
    """]
    execute_commands(connection, commands)

create_database()
create_tables()
