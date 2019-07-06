# Simple-CURD-on-REST-FRAMEWORK
# Django Rest-Framework
## Installation
we can install django using pip



```python
pip install django==2.2.3
```
Afrer installing django we have to start a project 
```python
django-admin startproject projectname
```
As soon as we have a project folder we need to start an application in our project 
```python
cd prjectname 
django-admin startapp app_name
```
After that we need to install rest_framework
```python
pip install pip install djangorestframework

```
Add 'rest_framework' and 'app_name'to your INSTALLED_APPS setting.
```python 
INSTALLED_APPS = (
    ...
    'rest_framework',
    'webapp'  #app_name
)
 ```
Running the Prject:
```python 
  python manage.py runserver
 ```
1) To list all the repositories :localhost:8000/Git/repo
2) To list events of a repo:localhost:8000/Git/rep/?r_id=?
3) To list all the events :localhost:8000/Git/events
4) To list actors of an event:localhost:8000/Git/evt/?e_id=?
5) To list all the actors :localhost:8000/Git/actors
6) To update/delete event:localhost:8000/Git/event/id?
7)To add an event :localhost:8000/Git/add
