# lynda - Learning Django Course


This is the repository for the LinkedIn Learning course Learning Django. The full course is available from [LinkedIn Learning](https://www.linkedin.com/learning/learning-django-2).

With Django, you can take web applications from concept to launch in a matter of hours. It's a free and open-source framework that's designed on top of Python and supports data-driven architecture. In this course, learn what you need to know to get up and running with Django. Instructor Caleb Smith walks through creating a brand-new Django project, defining a data model and fields, querying the database, and using the framework's built-in URL handlers, views, and templates to structure the rest of the back end. Plus, learn how to incorporate CSS and JavaScript to enhance the style and usability of your Django templates.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `master` branch holds the final state of the code when in the course.

The github link for the original course repo is [here](https://github.com/LinkedInLearning/learning-django-2825501)

## Project Steps
1. To create a django project navigate to the project folder in the terminal window and enter: 
    `$ django-admin startproject <project_name>`

2. To run the project, navigate to the created django project folder and type in the terminal:
    `$ python manage.py runserver`

3. After running project, can view the webpage by navigating to a browser and typing `localhost:8000`

4. To create an app, in the django project folder:
    `$ pythob manage.py startapp <app_name>`

5. Do something else
