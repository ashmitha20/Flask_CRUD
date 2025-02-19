from bson.objectid import ObjectId
from app.models import UserModel

class UserService:
    @staticmethod
    def create_user(data):
        user = {
            "name": data["name"],
            "email": data["email"],
            "password": data["password"],  # Consider hashing the password for security
        }
        return UserModel.create_user(user)

    @staticmethod
    def get_users():
        users = UserModel.get_users()
        for user in users:
            user["_id"] = str(user["_id"])
        return users

    @staticmethod
    def get_user_by_id(user_id):
        user = UserModel.get_user_by_id(ObjectId(user_id))
        if user:
            user["_id"] = str(user["_id"])
        return user

    @staticmethod
    def update_user(user_id, data):
        return UserModel.update_user(ObjectId(user_id), data)

    @staticmethod
    def delete_user(user_id):
        return UserModel.delete_user(ObjectId(user_id))
