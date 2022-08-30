# eligy Project 

The project is focused on the full cycle deployment for a conatinerized application. Below are the chronological flow of achieving this.

# 1
Create a public repo: https://github.com/Ribo01/eligy

#2 
 Write a basic application that can make API calls. the preferred language Python. A basic script was written to make simple API calls using the reques modules. The ain was to make a simple API call to a public request DB for API call test: htps://jsonplaceholder.typicode.com/todos1. The 2 main method adopted was a "GET" Method and a "POST" method.
 
 #3 
 The third step was to write a simple docker scripts to containerize the application and push to a container registry Docker HUB : https://hub.docker.com/repository/docker/08036044312/eligy_test 
 
image pull : 08036044312/eligy_test

#4 
the final step was to deploy the build application using Helm into a cluster. 
Helm scripts and deployment in eligy1-deployment. Helm version is v.2.16.3
