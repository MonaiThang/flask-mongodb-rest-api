
## Setup/installation Instructions
### MongoDB database
1. Install MongoDB via brew:
   ```bash
   brew tap mongodb/brew
   brew update
   brew install mongodb-community
   ```
2. Start MongoDB service:
   ```bash
   brew services start mongodb-community
   ```
3. Install MongoDB Compass, a MongoDB client with GUI from https://www.mongodb.com/try/download/compass
4. Open MongoDB Compass and create a connection to local MongoDB using the connection string below:
   ```bash
   mongodb://localhost:27017
   ```
5. Once connected to the database, select the "Databases" tab. Click the "Create database" button to create a new database. Use these settings below:
   - Database: blue-api
   - Collection name: articles

### Python application
1. Clone the source code from the repository.
2. Install Python version 3.9, you can download Python from https://www.python.org/downloads/
3. Install pipenv by follow the instructions from its documentation page https://pipenv.pypa.io/en/latest/install/#installing-pipenv
4. Browse the cloned source code directory and install Python packages as defined in Pipfile:
    ```bash
    pipenv install
    ```
5. Activate the pipenv:
    ```bash
    pipenv shell
    ```
6. Create an .env file at the root of the source code directory and fill in database connection details below using the matching information from database setup section:
    ```env
    DB_HOST=localhost:27017
    DB_NAME=blue-api
    ```
7. Run flask application:
    ```bash
    # These environment variables below can be skipped if they are defined in `.flaskenv`
    export FLASK_APP = src/__init__.py
    export FLASK_ENV = development
    export FLASK_DEBUG = 1
    flask run # or python -m flask run
    ```
8. You can then use REST API client e.g. Postman with the application. Note that the application port is 5000, so the base URL will be http://localhost:5000
9. To use Pytest, run this command below the project root directory:
    ```bash
    pytest
    ```