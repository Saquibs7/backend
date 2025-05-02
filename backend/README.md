# Project Title

## Description
This project is a Python application that runs inside a Docker container. It is designed to demonstrate how to containerize a Python application using Docker.

## Prerequisites
- Docker installed on your machine
- Basic knowledge of Docker and Python

## Getting Started

### Building the Docker Image
To build the Docker image for this application, navigate to the `backend` directory in your terminal and run the following command:

```
docker build -t my-python-app .
```

### Running the Docker Container
Once the image is built, you can run the Docker container using the following command:

```
docker run -it --rm my-python-app
```

### Accessing the Application
The application will start running as specified in the `CMD` instruction of the Dockerfile. You can access it as needed based on the functionality defined in `app.py`.

## Dependencies
The required Python packages are listed in the `requirements.txt` file. Make sure to update this file as needed to include any additional dependencies.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.