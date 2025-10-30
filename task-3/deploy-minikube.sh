#!/bin/bash
echo "Configuring Docker to use Minikube's daemon..."
eval $(minikube docker-env)

# Build the Docker image (using Minikube's daemon)
echo "Building Docker image..."
docker build -t task-manager:latest ./app

# Create namespace and deploy application
echo "Deploying to Kubernetes..."
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml

# Wait for deployment
echo "Waiting for deployment to be ready..."
kubectl -n task-manager wait --for=condition=available --timeout=300s deployment/task-manager

# Get the application URL
echo "Getting application URL..."
MINIKUBE_IP=$(minikube ip)
echo "Add the following line to your /etc/hosts file:"
echo "$MINIKUBE_IP task-manager.example.com"

# Check deployment status
echo -e "\nDeployment Status:"
kubectl -n task-manager get pods
kubectl -n task-manager get svc
kubectl -n task-manager get ingress

echo -e "\nApplication is deployed!"
echo "To access the application:"
echo "1. Add the above host entry to your /etc/hosts file"
echo "2. Access the API at: http://task-manager.example.com"
echo "3. Test the API with: curl http://task-manager.example.com/health"
echo -e "\nTo test auto-scaling, run:"
echo "kubectl -n task-manager get hpa task-manager -w"
echo "In another terminal, run: while true; do curl http://task-manager.example.com/load-test; done"
