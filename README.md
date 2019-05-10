# Web Application Security Challenge

## Introduction 

The Python Flask application has very basic security vulnerabilities which could be used for learning web application security.
The application has basic setup for user registration, sign in, password change and session management.

## Installation 

There are two options to set this project in the local machine and the other using docker 

> Warning: 
Never run this docker instance or the application exposed to the untrusted network. It could lead to compromise of the system. The author claims no responsibility of any damages caused because of this.

### Local Installation 

Clone the repository, install the packages and run 

```
git pull https://github.com/vskram21/SecChallenge.git
cd SecChallenge
pip -m install requirements.txt
cd src
flask run

```

### Docker 

If you choose to run this application on docker you could run 

```
docker pull kryptor21/secchallenge
docker run -p 5000:5000 kryptor21/secchallenge

```

The application would be running on port 5000 on your localhost.

## Credentials

The are two accounts in this application and the username and password listed below, 

- admin - admin
- user - user

You could also register yourself and get your account created.


## What is currently in place

Currently following vulnerabilties could be tested for,

1. Template Injection
2. Deserialization 
3. CORS - Make a cross domain request and read the response from a different domain
4. CSRF - Change the password of the user
