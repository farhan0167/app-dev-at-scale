# How to Scale your Application using Docker

You just developed a prototype or application based off the idea you had, and you deploy the application. While you were developing, you were probably dealing with only one user traffic or a max of, let's say, 5 users. Everything was going great, and your app is a success. On day 1, you have 10 users, followed by 50 in day 2, and by the end of the week you suddenly see a spike in traffic- there's 500 people trying to access your app's services. Your server is probably very slow or inaccessible to some users. Users start turning away, and what could've been the next startup just died down.

In this repository, I walk you through how you can address this very problem, and ensure your application is not only able to take the load of several thousand more users but is also able to scale.


## A Starter Flask App

To start off, let's assume we developed a simple Flask app. It processes some request and returns a service to a user. While development, if you are following their quickstart guide, you are most likely building something that looks like this:

![simple flask app](assets/1.jpeg)

You have yourself, querying the server. Everything is great.

## What happens when there are multiple users?

Eventually when you deploy your application as is and there are a lot of users trying to access your application, your server is fighting tooth and nail to serve every single request coming in. Thats what servers are supposed to do. You could expect your server to be really slow or in some cases, just crash.

![simple flask app with many users](assets/2.jpeg)

## Solution: Load Balancing

To solve this problem, what we can do is containerize our application and make multiple copies of it. Let me take a step back and explain what I mean by containerize your application. In simple words, what you will do is take that flask application you developed, and package into mini servers whose sole purpose of existence is to run the server. We call these mini servers, containers. One way to think of containers are shipping containers that is able to fit multiple goods of standard size and specification. Our container will load the flask app. Once you set up how the container will accept your flask app, you can spin up multiple copies of the same flask container. In the picture below, that is represented on the right. Now let's place a load balancer in the middle, and let's consider the load balancer to be a server whose sole job is to take a request come in from a user and route it to one of the containers.

![docker containers](assets/3.jpeg)

Now the users will make request to the load balancer who will distribute traffic evenly across all the containers hosting the flask app you spun up earlier. 

You are in charge of how you want the load balancer to distribute traffic. And you are also in charge of how many copies of the flask app you want to create. All you need to worry about is your flask app code, and a few specifications on how you want to make the containers and how you want the load balancer to behave.

Note: This is work in progress. More will be written soon.
