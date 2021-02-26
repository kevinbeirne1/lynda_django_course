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
    `$ python manage.py startapp <app_name>`

5. After creating app need to add it to the project. within the project folder open settings.py and scroll down to **INSTALLED_APPS** and add the app name

6. In the app folder, add model information to __*models.py*__

7. Add the migrations, in CLI type
    `$ python manage.py makemigrations`
To show migrations, type
    `$ python manage.py showmigrations`

8. To apply migrations,
    `$ python manage.py migrate`

9. Was outside the scope of the course to go create a management command, so just copied a pre-created one into the app folder. The CSV data to be import was added to the project folder

10. Data imported to the project by running:
    `$ python manage <command_file_name>`

11. In `admin.py` in the project folder, create a class that inherits from **admin.ModelAdmin**. Add an **admin.register** decorator to this class with the model it's associated with as an argument. eg in _admin.py_
```
from django.contrib import admin
from models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    pass
```

12. Create a superuser. In project folder in cli type the following, and follow the prompts. (tutorial password was - learningdjango):
`python manage.py createsuperuser` 

13. Respectively defined *\_\_str\_\_* and _list\_display_ in **models.py** and **admin.py**, 

14. Open django interactive shell: 
    `$ python manage.py shell

15. Within the django shell, import the model to be queried (regular python way). Can call a number of query functions on the model object
```
>>> from <app_name>.models import <model_name>
>>>
>>> <model_name>.object.all()  # Return all objects in queryset
>>> model_object = <model_name.object.all()[0]  # assign first object to variable
>>> model_object.id  # return object id
>>> model_object.<field>  # return object field
>>> <model_object>.object.get(<field>=<value>) # get object with field equal to the value
# get will raise an error if no object with field or multiple objects with same field 
```

16. In _urls.py_ in project folder, add the urls to **urlpatterns** variable

17. In _views.py_ in app folder, created stub views that are used when the urls in _urls.py_ are called 