import os


# Get the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# MongoDB
MONGODB_SETTINGS = {
    'db': 'test',
    'host': 'localhost',
    'connect': False
}

# Enable the TESTING flag to disable the error catching during request handling
# so that you get better error reports when performing test requests against the application.
TESTING = True

