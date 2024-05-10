from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
                  """)

    cursor.execute("""
        drop table if exists budgets;
                  """)
    
    cursor.execute("""
        drop table if exists expenses;
                  """)
    
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
            create table users (
                id SERIAL PRIMARY KEY,
                username text UNIQUE,
                password text); 
                   """)

    cursor.execute("""
            create table budgets (
                id SERIAL PRIMARY KEY,
                budget text,
                user text); 
                   """)
    
    cursor.execute("""
            create table expenses (
                id SERIAL PRIMARY KEY,
                budget text,
                expense text,
                sum integer); 
                   """)
    
    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
