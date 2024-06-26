from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row[1], row[2]) if row else None


class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_user(self, username):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        user = get_user_by_row(row)

        return user


    def create(self, user):
        cursor = self.connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self.connection.commit()

        return user

    def delete_all(self):
        cursor = self.connection.cursor()

        cursor.execute("delete from users")

        self.connection.commit()


user_repository = UserRepository(get_database_connection())
