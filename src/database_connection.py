import sqlite3
import os


def get_database_connection():
    dirname = os.path.dirname(__file__)

    try:
        load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
    except FileNotFoundError:
        pass

    TODOS_FILENAME = os.getenv("TODOS_FILENAME")
    TODOS_FILE_PATH = os.path.join(dirname, "..", "data", TODOS_FILENAME)

    DATABASE_FILENAME = os.getenv("DATABASE_FILENAME")
    DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

    connection = sqlite3.connect(DATABASE_FILE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
                  """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
            create table users (
                username text primary key,
                password text); 
                   """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
