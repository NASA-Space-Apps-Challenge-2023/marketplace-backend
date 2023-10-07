# NASA Open Science Marketplace - Backend API

This project provides a backend API for managing lab spaces, users, and reservations.

## Project Structure

The project follows a clean architecture and has been organized into various folders as below:

```
.
├── app
│ ├── main.py: Entry point of the application
│ └── server: Contains the main application logic
│ ├── app.py: FastAPI application initialization
│ ├── config.py: Configuration related code
│ ├── database: Contains database related code
│ ├── dependencies.py: Application dependencies like database session, authentication, etc.
│ ├── models: Database models
│ └── routes: API endpoints
├── db
│ └── docker-compose.yaml: Docker Compose file to set up MongoDB database
├── static: Contains static files like images and icons
└── tests: Contains test cases for the API
```


## Getting Started

### Prerequisites

- Python 3.7+
- Docker and Docker Compose (if using Docker to manage MongoDB)

### Installation

1. Clone the repository:
2. Set up MongoDB:
  - Using Docker:
    ```shell
    cd db
    docker-compose up -d
    ```
  - Or, configure your own MongoDB and update `app/server/config.py` with your connection credentials.
3. Install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```
4. Run the App:
    ```shell
    python app/main.py
    ```

## API Documentation

Once the application is running, API documentation can be accessed at http://localhost:8000/docs.

## License

This project is licensed under the [Apache License](LICENSE).
