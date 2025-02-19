from app import mongo

class UserModel:
    @staticmethod
    def create_user(user):
        return mongo.db.users.insert_one(user)
    
    @staticmethod
    def get_users():
        return list(mongo.db.users.find({}, {"password": 0}))

    @staticmethod
    def get_user_by_id(user_id):
        return mongo.db.users.find_one({"_id": user_id}, {"password": 0})
    
    @staticmethod
    def update_user(user_id, updated_data):
        return mongo.db.users.update_one({"_id": user_id}, {"$set": updated_data})
    
    @staticmethod
    def delete_user(user_id):
        return mongo.db.users.delete_one({"_id": user_id})
