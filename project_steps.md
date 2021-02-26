# lynda - Learning Django Course

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

18. The following syntax is used in the django templates
```
{{variable}}
{% tag %}
{{variable|filter}}

---Variable---
# in template
<h3>{{pet.name}}</h3>

# resulting HTML
<h3>Scooter</h3>


---Filters---
# in template
<h3>{{ pet.name|capfirst }}</h3> # sets it to capitalised

# resulting HTML
<h3>Scooter</h3>


---Loops---
# in template
{% for pet in pets %}
    <li>{{ pet.name }}</li>
{% endfor %}

# resulting HTML
<li>Scooter</li>
<li>Pepe</li>
...


---URL Tag---
# in template
{% url 'home' %}
{% url 'pet_detail' pet.id %}

# resulting HTML
/
/adoptions/1/

``` 

19. Course provided a base.html for a template. To use in the base.html file add a `{% block content %}` tag. Then in the template that is inheriting, list the extended class on the first line and place a content tag around the template information.
```
<!-- in base.html -->
<h1>
    ...
    	...
            {% block content %}
            {% endblock %}
</h1>


<!-- in sub-template -->
{% extends 'base.html' %}
{% block content %}
<div class=something>
    ...
</div>
{% endblock %}
```

20. To add static objects (eg images, files) add `{% load static tag %}` to the first line of the html template