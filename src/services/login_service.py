from entities.user import User
from repositories import user_repository 

class LoginService:
    def __init__(self, user_repository):
        self.user = None
        self.user_repository = user_repository

    def login(self, username, password):

        user = self.user_repository.find_user(username)

        if not user or user.password != password:
            print("not ok")

        self.user = user

        return user

    def logout(self):
        self.user = None


