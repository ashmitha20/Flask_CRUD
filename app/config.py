import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/userdb")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
