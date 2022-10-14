import psycopg2

# To resolve the path for the config file
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from database_config import username, password, host, port
from create_database_tables import execute_commands


def test_data():
    connection = psycopg2.connect(
        host = host,
        database = "postgres",
        user = username,
        password = password,
        port = port
    )

    commands = ["""INSERT INTO book (book_name, publisher_id, copy_count)
    VALUES ("Silmarillion", 0, 5),
    ("test_book", 1, 2000),
    ("")
    """]

    execute_commands(commands)


