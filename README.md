# Notes Management App

This repository contains a Dockerized Django application for managing personal notes.

## Getting Started

To run the Django application locally using Docker, follow these steps:

1. **Clone the repository:**

    ```
    git clone https://github.com/vishnu-thadathil/Notes-Management
    cd Notes-Management/
    ```

2. **Start the Application:**

    Run the following command to start the application:

    ```
    cd notes_management/
    docker-compose up
    ```

    This command builds the Docker images and starts the containers for the Django application.

3. **Access the Django application:**

    Open your web browser and go to http://localhost:8000.

4. **Stop the Application:**

    To stop the application and remove the containers, press Ctrl + C in the terminal where docker-compose up is running. Then run:

    ```
    docker-compose down
    ```
