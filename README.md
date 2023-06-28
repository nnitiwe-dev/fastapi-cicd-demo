# FastAPI Application Deployment Pipeline 101
Welcome to the FastAPI Application Deployment Pipeline repository! This repository contains the code and configuration files necessary for deploying a basic FastAPI application using an automated CI/CD pipeline.

## Folder Structure
- `.github/workflows/:` This directory houses the GitHub Actions workflow files defining the CI/CD pipeline.
- `app/:` Contains the main code files for the FastAPI application.
- `tests/:` Includes the test code files to verify the functionality of the FastAPI application.
- `config/aws/:` Contains the CloudFormation template for provisioning AWS infrastructure.

  
## Pipeline Overview
The pipeline is triggered by events like code pushes or pull requests. It automatically builds, tests, and deploys the FastAPI application to an EC2 instance on AWS. The process includes infrastructure provisioning, code deployment, and automated testing.

## Get Started
1. Set up your AWS credentials and secrets in the GitHub repository's settings to securely access AWS resources.
2. Configure the pipeline by modifying the workflows in the .github/workflows directory to match your specific deployment requirements.
3. Customize the FastAPI application in the app directory to suit your project need
   
Feel free to explore the repository for more details on the pipeline setup and configuration.
