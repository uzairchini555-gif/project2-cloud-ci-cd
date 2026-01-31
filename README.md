## Project 2 - CI/CD Auto Deploy Python App

## Overview
This is a python FastAPI backend application deployed on AWS EC2 with a fully automated CI/CD pipeline using Github Actions and Docker. Every code push automatically rebuilds the Docker container on EC2 and updates the app without manual intervention.

## Problem 
In a real-world cloud/DevOps workflow, manaully deploying apps after each code change is error-prone and time-consuming. Project 2 solves this by automating deployment so that updates are immediately reflected in the running app.


## Tech Stack
- Python 3.11 (FastAPI) - Backend API
- Docker - containerization
- AWS EC2 - Cloud hosting
- Girhub Actions - CI/CD Pipeline
- Linux (ubuntu) - Server OS

## Key Features
- Automatic deployment after each git push
- Dockerized app ensures consistent envioronment locally and on EC2
- Eliminates manula SSH and container rebuilds 
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
 #clone the repo
git clone https://github.com/<your-username>/project2-cloud-ci-cd

# Go into project folder
cd project2-cloud-ci-cd

# Build the Docker image
docker build -t project2-app .

# Run the container on port 8000
docker run -d -p 8000:8000 --name project2 project2-app

# Test it locally
curl http://localhost:8000


## Result / Demo
- After each push, Github Actions deploys the latest code automatically
- The EC2 container updates without manual SSH
- Browser shows the latest version immediately
