import os.path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = f'sqlite:///' + os.path.join(BASE_DIR, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
