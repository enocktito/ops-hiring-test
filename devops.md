# Quatro DevOps test

The goal of this test is to assess your familiarity with setting up a full CI/CD system. 
You'll be building CI/CD that will assure the continuous delivery / continuous integration of the project 
i.e when the dev push on a specific branch in our case (master/main)
 the CI/CD will test and deploy the code to the server that we provided to you.

# Task
Your task is to build a full CI/CD which will deploy this project to the server we provided to you:
  
- You have to use `docker` and `docker-compose` to build the project image which will run on the server.

- You have to install and configure postgres on the server. And authorize the user to connect from a remote machine.

- You have to install a web server `nginx` that will help to access to the project when we access to http://85.159.209.178

- The CI/CD shouldn't be down during a new release( **ZERO Downtime** ). You have to use `docker-swarm`

PS: Don't forget the security measures when you are setting up your CI/CD environment 
and feel free to configure it like it is your own server.

Please refer to the `README.rst` to know to setup the project.
