from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._user = None
        self.connection = connection

    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            print("not ok")

        self._user = user

        return user

    def logout(self):
        self._user = None

    def find_user(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create_user(self, username, password, login=True):
        cursor = self._connection.cursor()

        if self.find_user(username) != '':
            print("not ok")
            pass

        else:
            user = self.find_user(username)

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def get_current_user(self):
        return self._user
