import psycopg2

# To resolve the path for the config file
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from database_config import username, password, host, port

def create_database():
    connection = psycopg2.connect(
        host = host,
        database = "postgres",
        user = username,
        password = password,
        port = port
    )

    connection.autocommit = True

    cursor = connection.cursor()

    
    commands = "CREATE DATABASE library"

    cursor.execute(commands)
    connection.close()

def create_tables():
    print("hello")

create_database()
