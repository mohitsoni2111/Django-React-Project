1. `pip install virtualenv`
2. `python -m virtualenv venv`
3. `.\venv\Scripts\activate`
4. `pip install django`
5. Install nodeJS
6. npm install -g npm
7. pip install djangorestframework
8. django-admin startproject crud
9. This will create a folder crud -> crud.
10. I like to work with base so, rename the parent crud folder to something else and move the child outside of parent scope (inside BACKEND), then delete the parent folder.
11. `django-admin startapp api`
12. Go to crud -> settings.py file and add "rest_framework" and "api" under INSTALLED_APPS
13. Create a new urls.py file under api folder
14. Create a fucntion def home(request) under api -> views.py.
15. Update the crud -> urls.py to include the path of api.urls by adding new urlpattern i.e. *path('', include('api.urls'))*
16. `python .\manage.py makemigrations`
17. `python .\manage.py migrate`
18. `python .\manage.py runserver`
19. `pip install django-cors-headers` and follow website for update INSTALLED_APPS, MIDDLEWARE, CORS_ALLOWED_ORIGINS 