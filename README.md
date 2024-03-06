# Jenkins Pipeline for Dockerized Flask App and Nginx Proxy

This repository contains Jenkins pipeline scripts and Docker configurations for building and deploying a Flask web application and an Nginx reverse proxy.

## Overview

The Jenkins pipeline consists of three jobs:

1. **Job 1: Build and Push Flask App Docker Image**
   - This job pulls the code from the specified GitHub repository.
   - Builds a Docker image for a Python Flask web application that interacts with the local Docker engine to get the list of running containers.
   - Pushes the Docker image to Docker Hub.

2. **Job 2: Build and Push Nginx Proxy Docker Image**
   - This job modifies the default Nginx Dockerfile, adding a proxy pass to the Flask App container.
   - It injects source IP information into the request headers.
   - Pushes the modified Nginx Docker image to Docker Hub.

3. **Job 3: Run Docker Containers and Verify**
   - This job:
     - Pulls the Flask App Docker image and the modified Nginx Docker image from Docker Hub.
     - Runs both containers, exposing the Nginx container ports only on the local Jenkins machine.
     - Sends a request to verify that the communication between the Flask App and Nginx containers is successful.
     - Finishes successfully if the verification request is successful.

## Usage

### Prerequisites
- Jenkins is installed and configured.
- Docker is installed on the Jenkins machine.

### Set Up Jenkins Pipeline
1. Create a new pipeline job in Jenkins.
2. Configure the pipeline to pull the Jenkinsfile (Groovy script) from this GitHub repository.

### Environment Variables
Make sure to set the following environment variables in Jenkins or directly in the Jenkinsfile:

- `GITHUB_REPO_URL`: URL of the GitHub repository containing the Flask App code.
- `DOCKERHUB_USERNAME`: Your Docker Hub username.
- `DOCKERHUB_PASSWORD`: Your Docker Hub password or access token.

### Running the Pipeline
1. Trigger Job 1 manually or set up a webhook to trigger it on code push.
2. Once Job 1 succeeds, trigger Job 2 manually or set up a webhook.
3. After Job 2 completes successfully, trigger Job 3 manually to deploy and verify the containers.
