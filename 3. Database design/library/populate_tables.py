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

def test_data():
    connection = psycopg2.connect(
        host = host,
        database = "postgres",
        user = username,
        password = password,
        port = port
    )

    commands = ["""
    
    """]

