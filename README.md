# MLOps Flask Demo

## Run locally
python3 -m venv .dk
source .dk/bin/activate
pip install -r requirements.txt
python app.py

Open http://localhost:5000

## Test
pytest

## Build Docker image
docker build -t docker-flask-app:latest .

## Run container
docker run -p 5000:5000 docker-flask-app:latest

## Jenkins
Create a Pipeline job connected to this Git repository. Jenkins will run the Jenkinsfile stages:
Checkout -> Create Python Environment -> Install Requirements -> Test -> Build Docker Image

## Git Workflow

This project uses Git and Github for version control.
_Main branch stores the stable project code.
_Feature branches are used for new changes.
_Changes are committed and pushed to Github.
_Pull Requests are used to review and merge changes.

