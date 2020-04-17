# KNativePythonDemo
KNativePythonDemo for Python application Deployment on Kubernetes cluster

This example shows you how to structure your code as a class in Flask-Classful API framework.

# On your local machine where you run app.py, you can hit the the API by calling:
localhost:8080/

# Build the container on your local machine
docker build -t {username}/helloworld-python .

# To push the container to auroradevacr Azure Container Registry
az acr login --name auroradevacr
docker tag {username}/helloworld-python auroradevacr.azurecr.io/{username}/helloworld-python
docker push auroradevacr.azurecr.io/{username}/helloworld-python

