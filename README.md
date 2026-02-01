## Project 2 - CI/CD Auto Deploy Python App

## Overview
This is a python FastAPI backend application deployed on AWS EC2 with a fully automated CI/CD pipeline using Github Actions and Docker. Every code push automatically rebuilds the Docker container on EC2 and updates the app without manual intervention.

## Problem 
In a real-world cloud/DevOps workflow, manaully deploying apps after each code change is error-prone and time-consuming. Project 2 solves this by automating deployment so that updates are immediately reflected in the running app.


## Tech Stack
- Python 3.11 (FastAPI) - Backend API
- Docker - containerization
- AWS EC2 - Cloud hosting
- Github Actions - CI/CD Pipeline
- Linux (ubuntu) - Server OS

## Key Features
- Automatic deployment after each git push
- Dockerized app ensures consistent environemnt locally and on EC2
- Eliminates manual SSH and container rebuilds 
- Handles container reatart automatically

## Challenges Faced 
- Docker build errors and conntainer crashes
- Python syntax errors during app update 
- Misconfiguration of Github Actions SSH step (script typo!)
- Ensuring the app listens on 0.0.0.0 for external access

## Architecture / Workflow

Laptop (code push)
       |
Github Actions (CI/CD)
       |
SSH to EC2 -> git pull, docker build and run
       |
Docker container runs FastAPI app
       |
Browser access -> http://<EC2_PUBLIC_IP>:8000

## How to run locally
```bash
git clone https://github.com/<your-username>/project2-cloud-ci-cd
cd project2-cloud-ci-cd
docker build -t project2-app .
docker run -d -p 8000:8000 --name project2 project2-app
curl http://localhost:8000

## Result / Demo
"Every push to main triggers a Github Actions workflow that:
- Builds a Docker Image
- Connects to EC2 via SSH 
- pulls latest code
- Rebuilds and Restarts the container"

## Demo Screenshot

![App running in browser](images/browser-output.png)

