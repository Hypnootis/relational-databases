import psycopg2

def create_database():
    conn = psycopg2.connect(
        host="localhost",
        database="",
        user="",
        password=""
    )

def create_tables():
    print("hello")
