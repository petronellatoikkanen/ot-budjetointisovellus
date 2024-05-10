from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)

class LoginService:
    def __init__(self):
        self.user = None
        self.user_repository = default_user_repository

    def login(self, username, password):
        user = self.user_repository.find_user(username)

        if not user:
            print("user not found, please create an account")
            return False
        elif user.password != password:
            print("wrong password, please try again")
            return False
        else:
            self.user = user
            return user

    def logout(self):
        self.user = None


login_service = LoginService()  