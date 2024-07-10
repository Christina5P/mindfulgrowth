# Introduction

# Content

# Project Set Up
## User Stories
## Blog Plan


## Mindmap

![alt text](image-10.png)
link to my mindmap: https://miro.com/app/board/uXjVK1IKqsk=/

## Relationship diagram ERD

![alt text](image-11.png)

Link: https://drive.google.com/file/d/1SYwaMzGs6PuOuEuA6Yi4T2Q0p8dvmSvd/view?usp=sharing

## Wireframes

Wireframe is created in https://balsamiq.cloud/srvezeo/phn02iw/r3EBE
Home page:
![alt text](image-6.png)
Blog page:
![alt text](image-7.png)
Courses:
![alt text](image-8.png)

Blogpost:
![alt text](image-9.png)


# Features

## Home Page
## Blog Page
## Nav Bar
## Footer
## Register section

# Setting up workspace
### Run this command to install django:
 pip3 install 'django<4'  
### Next, install these libraries: 
pip3 install dj_database_url psycopg2
pip3 install dj3-cloudinary-storage
### Create a requirements.txt file to save all the installed libraries:
pip3 freeze --local > requirements.txt
### You need to create a project and add my apps:
django-admin startproject mindfulgrowth
python3 manage.py startapp blog
Remember to add your apps in to the 'INSTALLED_APPS' in setting.py
 ### Add your DB and CLoudinary library to your project:
 Copy the DATABASE_URL
 create a new file manual with name: env.py
 This file need to be placed in the project cataloge
 Import the os library:
 import os
Set environment variables:
os.environ.setdefault(
    "DATABASE_URL", "postgres://uottaphddte:1ZsY6k60KNPN@ep-gentle-mountain-a23bxz6h.eu-central-1.aws.neon.tech/vocal_moan_poem_31644")
 
os.environ.setdefault(
    "SECRET_KEY", "django-insecure-%s0!8rr$!pbkcomh1bmeybs4nldjtws=8n%pffttkm%(-nrrma")    

os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://618768418781469:Q8KVKcOdIzeC4kCaKocmseNCHmM@dvh69l0yv")

os.environ["SECRET_KEY"] = "mysecretkey"

Add the env.py-file to the setting.py file with commando in the file:
import env

You also need to put this in the setting.py file under :

ALLOWED_HOSTS = ['8000-christina5p-mindfulgrow-0ffy6j8ksnb.ws.codeinstitute-ide.net',
'mindfulgrowth-5f753257331e.herokuapp.com',
'8080-christina5p-mindfulgrow-0ffy6j8ksnb.ws.codeinstitute-ide.net']

CSRF_TRUSTED_ORIGINS = [
    "https://*8000-christina5p-mindfulgrow-0ffy6j8ksnb.ws.codeinstitute-ide.net",
    "https://*mindfulgrowth-5f753257331e.herokuapp.com" 
]

Dont forget to add apps and libraries in 

INSTALLED_APPS = []

Before deploying on heroku make sure: DEBUG = False

### Create 3 new folders on the root directory: media, static, templates

### Create Procfile (needed for Heroku) on the root directory and inside the file type:
web: gunicorn basic_mind.wsgi
hint: It´s important to spell Procfile with a capital



# Feautures Implementented

# Design

# Testing
## Validating Test
## Python Test
## Manual Test

# Bugs
## Fixed Bugs
## Unfixed Bugs

# Technologies
### Python - Language of this project
### Javascript
### HTML
### CSS
### Django - 
### Cloudinary (for external image management)
### Code Institute Postgres Database server for PostgreSQL 
### Bootstrap
### Github - Save the project in a repository
### Heroku - Deploy it to a public website

# Deployment

For deploying, I use the Heroku app.
At first, you commit everything to GitHub.
In Heroku, you set up an app for the project and deploy the changes you make to the public site.



## Heroku
You connect the app to your repository in GitHub with the same name.
I chose to make a manual deployment, so I can see that everything goes ok and have control of my project.

You need to create an app for your project in Heroku.
In settings you also need to fill in the URL:s in Config Var
![alt text](image-1.png)

After that you go to Herokus deployment section 

![alt text](image-2.png)

Scroll down to the bottom and click the "deploy button

![alt text](image-3.png)

On the top at right hand side, you can click "open app" to see public site.
If there is any error, you can find the logs if you click "more" button.

![alt text](image-4.png)

## Git Hub / Gitpod
I created a repository in Git Hub and connected a project to the repository.
In the project, I worked with the canban and created the user stories there.
From Gitpod, I pushed my changes to GitHub with the commands 

When I add, deleated or changed anything, I committed them back to GitHub using the following commands in the codespace terminal: Git add .
Git commit -m"text"
Git push

To run a backend application in Gitpods terminal,
type: python3 manage.py runserver 

To see and implement changes in Django, type:
python3 manage.py makemigrations
pyhton3 manage.py migrate

## How to Fork
To fork this repository, click the "Fork" button at the top right corner of the main repository page. On the "Create a Fork" page, you can change the name of the repo if desired. Check the box if you want to copy the main branch or multiple branches (main is selected by default). Then, create the fork.

## How to Clone (An alternative to fork)
To clone the repository, you create a copy in your repository (with all files and history).
This creates a remote link to the original repo, allowing you to work in your copy and push changes back to the original.
Open your repo and click the green "Code" button on the right-hand side. The easiest way is to open it with GitHub Desktop.

You can read more information on cloning at the GitHub : https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

# Media
## Icons
## Images
## Font
## Databas
## Framework 

# Acknowledgement

### for tutoring Django:
https://youtube.com/playlist?list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&si=9t7TdLJVAM9BM9Ga
https://realpython.com/build-a-blog-from-scratch-django/#set-up-the-development-environment

### Wireframes:
https://balsamiq.cloud/

### Create ERD: 
http://draw.io

