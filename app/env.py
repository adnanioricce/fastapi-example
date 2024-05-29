import os

# get environment variables
def get_settings():
    SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL","")
    return { "SQLALCHEMY_DATABASE_URL": SQLALCHEMY_DATABASE_URL}