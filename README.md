## Project 2 - Cloud CI/CD Pipeline with Docker & AWS EC2

## Overview
This project demonstrates a real-world CI/CD pipeline where a containerized python web application is automatically build and deployed to an AWS EC2 instance using Github Actions

Any code change pushed to Github triggers an automated workflow that rebuilds the Docker iamge and redeploys the application - no manual SSH or restart required.

## Problem Statement
Manually deploying applications on server is:
- Error-prone
- Time-consuming 
- Not scalable

## Goal of the project
- implement CI/CD automation using Github Actions
- Eliminate manual deployment step
- Ensure the app behaves the same across environment using Docker 
- Deploy updates to AWS EC2 automatically on every push 

## Tech Stack
- Python 3.11 (FastAPI) - Backend API
- Docker - containerization
- AWS EC2 - Cloud hosting
- Github Actions - CI/CD Pipeline
- Linux (ubuntu) - Server OS

## How the CI/CD pipeline works
1. Developer pushes code to the main branch
2. Githu Actions workflow is triggered 
3. Workflow:
  - Checks out the latest code 
  - Build a docker image 
  - Connects securely to EC2 via SSH
  - stops the old container 
  - Runs the updated container 
4. Application is updated automatically 
✅ Zero manual intervention
✅ Repeatable and reliable deployments

## Project Structure 
Project-cloud-ci-cd
      | 
app/
    main.py
      |
images/ 
       browser-output.png
      |
Dockerfile
      |
requirements.txt
      |
README.md
      |
.github/
        workflows/
                  ci.yaml

## How to Run Locally
```Bash
git clone 
https://github.com/<Your-user>/project2-cloud-cd-cd.git
cd project-cloud-ci-cd

docker build -t project2-app .
docker run -d -p 8000:8000 --name project2 project2-app

curl http:/localhost:8000
```
## Live Demo 
http://<EC2_PUBLIC_IP>:8000

## Demo Screenshot 
![App is running in bowser](images/browser-output.png)

## Challenges Faced $ Solutions
- Docker build errors -> Resolved by analyzing logs and fixing image structure
- App not uploading after push -> Fixed CI/CD workflow misconfiguration
- SSH access issue -> Solved via IAM roles and security group best practise 
- Container resatrt problem -> Automated restart via Github Actions
These issues helped strengthen my understanding of real production problems.

## Key Learnings
- Practical CI/CD using Github Actions
- Docker image lifecycle and container management
- Secure EC2 deployment using SSH keys
- importance of automation in DevOps workflow
- Debugging production-like cloud issues 

## Future Improvements
- Deploy using kubernetes (EKS)
- Add Application Load Balancer 
- Implement blue-green deployments
- Add monitoring with CloudWatch

## Author 
Uzair Munir 
Aspiring Cloud / DevOps Engineer
