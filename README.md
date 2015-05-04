plexauth
========

This module provides a django authentication backend for authenticating against plex.tv.

Installing
----------

Install by placing the plexauth module in your python path.

Configuration
-------------

In the settings.py file for your project, ensure you have the following:

```
INSTALLED_APPS = (
	...
	'plexauth',
)
AUTHENTICATION_BACKENDS = (
    'plexauth.auth.PlexBackend',
)

AUTH_USER_MODEL = 'plexauth.PlexUser'
PLEX_ADMIN_USERS = ('admin_usernames')
PLEX_SERVER_NAME = 'your_server_nickname'
```