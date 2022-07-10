import os


# Get the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# MongoDB
MONGODB_SETTINGS = {
    'db': os.getenv('DB_NAME'),
    'host': os.getenv('DB_HOST'),
  # 'username': os.getenv('DB_USERNAME'),
  # 'password': os.getenv('DB_PASSWORD'),
    'connect': False
}
