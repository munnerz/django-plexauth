plexauth
========

This module provides a django authentication backend for authenticating against plex.tv.

Installing
----------

Install by placing the plexauth module in your python path.

Requirements
------------
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
