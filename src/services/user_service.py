from entities.user import User
from repositories import user_repository 

class UserService:
    def __init__(self, user_repository):
        self.user = None
        self.user_repository = user_repository

    def get_current_user(self):
        return self.user

    def get_users(self):
        return self.user_repository.find_all()
    
    def create_user(self, username, password):
        if self.user_repository.find_user(username):
            print("not ok, already exists")
            pass

        self.user = self.user_repository.create(User(username, password))

        return self.user
    