import psycopg2

# Resolve the path for the config file
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from database_config import username, password, host, port
from populate_tables import test_data

DBNAME = "discography"

# TODO: rethink this one through from the ground up!

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
   
    commands = ["""CREATE TABLE IF NOT EXISTS track (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        track_length INT
    )
    """
    """CREATE TABLE IF NOT EXISTS tracklist (
        id SERIAL PRIMARY KEY,
        track_id INT
    )
    """,
    """CREATE TABLE IF NOT EXISTS cd (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price REAL,
        genre VARCHAR(255),
        tracklist_id INT
    )
    """,
    """CREATE TABLE IF NOT EXISTS artist (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        discography_id INT
    )
    """,
    """CREATE TABLE IF NOT EXISTS discography (
        id SERIAL PRIMARY KEY,
        cd_id INT,
        cd_name VARCHAR(255)
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
        ALTER TABLE tracklist
        ADD CONSTRAINT fk_tracklist_trackid FOREIGN KEY (track_id) REFERENCES track(id),
        """,
        """ALTER TABLE cd
        ADD CONSTRAINT fk_cd_tracklistid FOREIGN KEY (tracklist_id) REFERENCES tracklist(id)
        """,
        """ALTER TABLE discography
        ADD CONSTRAINT fk_discography_cdid FOREIGN KEY (cd_id) REFERENCES cd(id),
        ADD CONSTRAINT fk_discography_cdname FOREIGN KEY (cd_name) REFERENCES cd(name)
        """,
        """ALTER TABLE artist
        ADD CONSTRAINT fk_artist_discographyid FOREIGN KEY (discography_id) REFERENCES discography(id)
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
