import os
import git
import subprocess

# User input
repo_url = input("Enter GitHub Repository URL (HTTP/SSH): ")
docker_hub_username = "your-dockerhub-username"

# Step 1: Clone Repository
def clone_repo():
    if os.path.exists("cloned_repo"):
        print("Deleting old repository...")
        os.system("rm -rf cloned_repo")
    
    print("Cloning repository...")
    git.Repo.clone_from(repo_url, "cloned_repo")
    print("Repository cloned successfully!")

# Step 2: Build Docker Image
def build_docker_image():
    print("Building Docker image...")
    os.system("docker build -t devops-automation-tool cloned_repo")
    print("Docker image built successfully!")

# Step 3: Push to Docker Hub
def push_to_docker_hub():
    print("Tagging and pushing image to Docker Hub...")
    os.system(f"docker tag devops-automation-tool {docker_hub_username}/devops-automation-tool:latest")
    os.system(f"docker push {docker_hub_username}/devops-automation-tool:latest")
    print("Image pushed to Docker Hub!")

# Step 4: Deploy to Kubernetes
def deploy_kubernetes():
    print("Applying Kubernetes deployment...")
    os.system("kubectl apply -f k8s-deployment.yaml")
    print("Application deployed on Kubernetes!")

# Run All Steps
clone_repo()
build_docker_image()
push_to_docker_hub()
deploy_kubernetes()

print("\n🚀 Automation Complete! Your app is now live on Kubernetes! 🎉")

