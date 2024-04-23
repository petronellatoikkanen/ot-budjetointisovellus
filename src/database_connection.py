import sqlite3
import os

def get_database_connection():
    dirname = os.path.dirname(__file__)

    BUDGETING_FILENAME = os.getenv("BUDGETING_FILENAME")
    BUDGETING_FILE_PATH = os.path.join(dirname, "..", "data", BUDGETING_FILENAME)

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
