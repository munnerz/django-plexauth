plexauth
========



![Screenshot](https://cloud.githubusercontent.com/assets/203583/7464347/62ecff22-f2ba-11e4-9146-bbd237b2fb93.png)


This module provides a django authentication backend for authenticating against plex.tv.

After properly setting up, you should be able to authenticate at /auth/login.

Installing
----------

Install by placing the plexauth module in your python path.

All requirements can be installed via pip:

```
pip install requests
pip install django
pip install django-bootstrap3
pip install django-activelink
```

Requirements
------------
* [requests](https://github.com/kennethreitz/requests) >= 2.7.0
* [django](https://github.com/django/django) >= 1.8.0
* [django-bootstrap3](https://github.com/dyve/django-bootstrap3)
* [django-activelink](https://github.com/j4mie/django-activelink) >= 0.4


Configuration
-------------

In the settings.py file for your project, ensure you have the following:

```
INSTALLED_APPS = (
	...
	'bootstrap3',
	'activelink',
	'plexauth',
)
AUTHENTICATION_BACKENDS = (
    'plexauth.auth.PlexBackend',
)

AUTH_USER_MODEL = 'plexauth.PlexUser'
PLEX_ADMIN_USERS = ('admin_usernames')
PLEX_SERVER_NAME = 'your_server_nickname'
```

In your urls.py file, add the following line

```
urlpatterns = patterns('',
	...
	url(r'^auth/?', include('plexauth.urls')),
)
```
