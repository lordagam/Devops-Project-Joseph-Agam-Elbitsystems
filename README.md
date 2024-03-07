# Jenkins Pipeline for Dockerized Flask App and Nginx Proxy

 This repository contains Jenkins pipeline scripts and Docker configurations for building and deploying a Flask web application and an Nginx reverse proxy.

## Overview

 The Jenkins pipeline consists of four jobs:
** Job 1: Checkout Repository

   - This job checks out the code from the specified GitHub repository.

** Job 2: Build and Push Flask App Docker Image

   - This job builds a Docker image for a Python Flask web application.
   - It interacts with the local Docker engine to get the list of running containers.
   - The Docker image is pushed to Docker Hub.

** Job 3: Build and Push Nginx Proxy Docker Image

   - This job modifies the default Nginx Dockerfile, adding a proxy pass to the Flask App container.
   - It injects source IP information into the request headers.
   - The modified Nginx Docker image is pushed to Docker Hub.

** Job 4: Run Docker Containers and Verify

   - This job pulls the Flask App Docker image and the modified Nginx Docker image from Docker Hub.
   - It runs both containers, exposing the Nginx container ports only on the local Jenkins machine.
   - The job sends a request to verify that the communication between the Flask App and Nginx containers is successful.
   - It finishes successfully if the verification request is successful.

** Usage
** Prerequisites

   - Jenkins is installed and configured.
   - Docker is installed on the Jenkins machine.

** Set Up Jenkins Pipeline

   - Create a new pipeline job in Jenkins.
   - Configure the pipeline to pull the Jenkinsfile (Groovy script) from this GitHub repository.

** Environment Variables

- Make sure to set the following environment variables in Jenkins or directly in the Jenkinsfile:

  -  GITHUB_REPO_URL: URL of the GitHub repository containing the Flask App code.
  -  DOCKERHUB_USERNAME: Your Docker Hub username.
  -  DOCKERHUB_PASSWORD: Your Docker Hub password or access token.

** Running the Pipeline

  -  Trigger Job 1 manually or set up a webhook to trigger it on code push.
  -  Once Job 1 succeeds, trigger Job 2 manually or set up a webhook.
  -  After Job 2 completes successfully, trigger Job 3 manually to deploy the modified Nginx container.
  -  Finally, trigger Job 4 manually to verify the communication between Flask App and Nginx containers.
