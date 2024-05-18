# User Management Flask Application

This project is a simple Flask application that provides a basic backend for managing user data. It uses PostgreSQL as the database and SQLAlchemy as the ORM (Object Relational Mapper) to interact with the database.

## Tech Stack
- Flask: A lightweight WSGI web application framework for Python.
- PostgreSQL: A powerful, open-source object-relational database system.
- SQLAlchemy: A SQL toolkit and ORM that gives application developers the full power and flexibility of SQL.
- Werkzeug: A comprehensive WSGI web application library. It is used here for password hashing.

## Database Model
The application uses a single User model to represent a user in the database. The model has the following fields:

- `id`: A unique identifier for each user. It is the primary key.
- `username`: The username of the user. It is unique and cannot be null.
- `email`: The email of the user. It is unique and cannot be null.
- `password`: The hashed password of the user. It cannot be null.

## Environment Variables

The application uses the `dotenv` package to load environment variables (`.env`). The PostgreSQL database URL (`SQLALCHEMY_DATABASE_URI`) for SQLAlchemy is set in the environment variables and loaded into the project.

## How to Run

1. You need to have Python and PostgreSQL installed on your machine.
2. Clone the repository or download the directory.
3. Install the necessary Python packages using pip or run `pip install -r requirements.txt`
4. Make sure your PostgreSQL server is running. Create a new database and set the database URL in your environment variables (`.env`).
5. Run the Flask application with `python app.py`

## Working

After running the Flask application, you can interact with it using the following endpoints:

1. Register a New User: Send a POST request to `/register` with the following JSON body:
   ```json
    {
        "username": "<username>",
        "email": "<email>",
        "password": "<password>"
    }
   ```
    This endpoint will create a new user with the provided username, email, and password. Email and password will be validated and the password will be hashed before being stored in the database.

2. List All Users: Send a GET request (or simply visit the route) to `/users`. This endpoint will return a list of all registered users in JSON format.
   
NOTE: These endpoints do not include any form of authentication or authorization. They are intended to serve as a starting point for building more complex Flask applications.