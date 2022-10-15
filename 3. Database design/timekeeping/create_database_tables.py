import psycopg2

# Resolve the path for the config file
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from database_config import username, password, host, port
from populate_tables import test_data

DBNAME = "timekeeping"

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
    commands = [f"CREATE DATABASE {DBNAME}"]

    try:
        execute_commands(connection, commands)
    except:
        print("Connection must be a psycopg2.connect() type!")

def create_tables():
    connection = psycopg2.connect(
        host = host,
        database = DBNAME,
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
        entry_date DATE,
        project_id INT,
        employee_id INT,
        hours_worked INT
    )
    """]

    execute_commands(connection, commands)

def add_constraints():
    connection = psycopg2.connect(
        host = host,
        database = DBNAME,
        user = username,
        password = password,
        port = port
    )
    commands = ["""
        ALTER TABLE timetable
        ADD CONSTRAINT fk_timetable_projectid FOREIGN KEY (project_id) REFERENCES project(id),
        ADD CONSTRAINT fk_timetable_employeeid FOREIGN KEY (employee_id) REFERENCES employee(id)
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
    connection.cursor().execute(f"DROP DATABASE IF EXISTS {DBNAME}")

drop_database()
create_database()
create_tables()

# Add test data
execute_commands(psycopg2.connect(host=host, database=DBNAME, user=username, password=password, port=port), test_data)

add_constraints()
