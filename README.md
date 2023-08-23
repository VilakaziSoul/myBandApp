# Django Straw Hats Band

This is a Django project that reimagines the Straw Hat Pirates as a rock band. Follow the steps below to build and run the application using `venv` and Docker.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/) and [virtualenv](https://pypi.org/project/virtualenv/)

## Build and Run with venv

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver

# Build and Run with Docker
# Clone the repository
git clone https://github.com/vilakazisoul/myBandApp
cd your-repo

# Build the Docker image
docker build -t my-band-app .

# Run a Docker container
docker run -p 8000:8000 my-band-app

