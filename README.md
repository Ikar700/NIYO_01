# NIYO_01: Task Management API

This repository contains a RESTful API for a simple task management system, developed as my entry for the NIYO group Backend Developer's Assessment.
The API provides user authentication, CRUD operations for tasks, data persistence, and input validation.

## Features

- **User Authentication**: Implemented using JSON Web Tokens (JWT) for secure authentication and authorization.
- **CRUD Operations**: Endpoints for creating, reading, updating, and deleting tasks.
- **Data Persistence**: Task data is stored in a database - SQLite, PostgreSQL, MySQL.
- **Input Validation**: Input data is validated to ensure data integrity and security.
- **Real-time Updates**: A WebSocket connection is established to stream task data updates in real-time.

## Technologies Used

- Python
- Django
- Django Djoser (For user authentication)
- Django REST Framework
- Django Channels (for real-time updates)
- JWT Authentication
- Database - PostgreSQL (hosted on render)

## Installation

1. Clone the repository:

       git clone https://github.com/Ikar700/NIYO_01.git

2. Navigate to the project directory:

        cd NIYO_01

3. Create and activate a virtual environment :

    python -m venv env
    
    ## On Linux-based Machines and macOS
        source env/bin/activate 
    ## On Windows, 
        use env\Scripts\activate

5. Install the required dependencies:

        pip install poetry
        poetry install

6. create a .env file in the NIYO folder.

        
7. Copy the keys in docs/.env.sample then paste into the NIYO/.env

8. Start the development server:

        python manage.py runserver

The API will be accessible at `http://localhost:8000/`.

## Documentation

The API endpoints, data models, .env for the environment variables and other relevant information are documented in the `docs` directory. Please refer to the documentation for detailed information on using the API.

Postman_workspace_link - https://www.postman.com/cloudy-shadow-362896/workspace/niyo/overview

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
