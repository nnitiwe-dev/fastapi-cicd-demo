#!/bin/bash

# Get the INSTANCE_ID and REGION values from GitHub Secrets
INSTANCE_ID=$(aws cloudformation describe-stacks --stack-name FastAPI_CICD_Stack101 --query 'Stacks[0].Outputs[?OutputKey==`MyEC2InstanceID`].OutputValue' --region $AWS_REGION --output text)
REGION=$AWS_REGION

# Get the public IP address of the EC2 instance
PUBLIC_IP=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --region $REGION --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)

# Get the public DNS name of the EC2 instance
PUBLIC_DNS=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --region $REGION --query 'Reservations[0].Instances[0].PublicDnsName' --output text)

# Print the URL of the FastAPI application
echo "FastAPI is accessible at:"
echo "http://$PUBLIC_IP:8000"
echo "or"
echo "http://$PUBLIC_DNS:8000"
