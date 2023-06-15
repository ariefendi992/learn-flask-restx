from dotenv import load_dotenv
import os

load_dotenv()

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    SECRET_KEY = str(os.getenv("SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
