#!/bin/bash

# Build and push Docker image
echo "Building Docker image..."
docker build -t task-manager:latest ./app
docker tag task-manager:latest your-registry/task-manager:latest
docker push your-registry/task-manager:latest

# Create namespace and deploy application
echo "Deploying to Kubernetes..."
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml
kubectl apply -f k8s/servicemonitor.yaml

# Check deployment status
echo "Checking deployment status..."
kubectl -n task-manager get pods
kubectl -n task-manager get svc
kubectl -n task-manager get ingress
