from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)


class UsernameExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class UserService:
    def __init__(self,user_repository=default_user_repository):
        self.user = None
        self.user_repository = default_user_repository

    def login(self, username, password):
        user = self.user_repository.find_user(username)

        if not user or user.password!=password:
            raise InvalidCredentialsError("Invalid username or password")

        self.user = user
        return user

    def logout(self):
        self.user = None
        return self.user

    def get_current_user(self):
        return self.user

    def create_user(self, username, password):
        if len(username) < 5 or len(password) < 8:
            raise InvalidCredentialsError ("Enter valid username (>4) and password (>7)")

        if self.user_repository.find_user(username):
            raise UsernameExistsError(f"Username {username} already exists")

        self.user = self.user_repository.create(User(username, password))

        return self.user


user_service = UserService()
