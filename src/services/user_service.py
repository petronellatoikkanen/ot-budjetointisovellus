from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)

class UserService:
    def __init__(self):
        self.user = None
        self.user_repository = default_user_repository

    def get_current_user(self):
        return self.user

    def get_users(self):
        return self.user_repository.find_all()
    
    def create_user(self, username, password):

        if self.user_repository.find_user(username):
            print(f"Username {username} already exists")
            return

        self.user = self.user_repository.create(User(username, password))

        return self.user
    

user_service = UserService()