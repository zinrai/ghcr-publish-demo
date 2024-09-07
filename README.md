# ghcr-publish-demo

"Hello World" API using Python and Falcon, containerized with Docker and automatically built and published to GitHub Container Registry (GHCR) using GitHub Actions.

## Features

- Simple Falcon API that returns a "Hello, World!" message
- Dockerized application
- Automated build and publish to GHCR using GitHub Actions

## Prerequisites

- Python 3.11
- Docker
- GitHub account with access to GHCR

## Local Development

1. Create and activate a virtual environment:
   ```
   $ python3 -m venv venv
   $ source venv/bin/activate
   ```

2. Install dependencies:
   ```
   $ pip install -r requirements.txt
   ```

3. Run the application:
   ```
   $ python3 main.py
   ```

4. Access the API at `http://localhost:8000/hello`

## Docker Usage

To build and run the Docker container locally:

1. Build the image:
   ```
   $ docker build -t hello_sample .
   ```

2. Run the container:
   ```
   $ docker run -p 8000:8000 hello_sample
   ```

3. Access the API at `http://localhost:8000/hello`

## GitHub Actions Workflow

GitHub Actions workflow that automatically builds and publishes the Docker image to GHCR when a new tag is pushed to the repository.

To trigger the workflow:

1. Create and push a new tag:
   ```
   $ git tag v1.0.0
   $ git push origin v1.0.0
   ```

2. The workflow will automatically run, building and publishing the image to GHCR with the tag `ghcr.io/zinrai/hello_sample:v1.0.0`

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
