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








## Q5: MLOps Failure Recovery and Rollback 
## Version Backup 
The working Docker image was saved as docker-flask-app:v1.
### Failure Simulation 
A faulty deployment was simulated using docker-flask-app:v2.
The faulty container exited with status code 1.
### Rollback 
The pervious stable image was restored using docker-flask-app:v1.
### Verfication 
The application was tested after rollback:
- GET / returned the applicationn status successfully.
- GET /predict returned the demo prediction successfully.
### Result
The faulty deployment was stopped and the previous working Docker image was successfully restored.