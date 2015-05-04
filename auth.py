from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

url = "https://plex.tv/users/sign_in.xml"

plex_headers = {"X-Plex-Product": "Custom Auth",
                "X-Plex-Version": "0.1",
                "X-Plex-Client-Identifier": "customauthapp",
                "X-Plex-Platform": "N/A",
                "X-Plex-Platform-Version": "0.1",
                "X-Plex-Device": "Python",
                "X-Plex-Device-Name": "Custom Plex Authenticator",
                "Accept-Language": "en"}

def plex_auth(username, password):
  import requests, xml.etree.ElementTree as etree

  tree = etree.fromstring(requests.post(url, 
                                        headers=plex_headers, 
                                        auth=(username, password)
                                      ).text)

  auth_token = tree.find("authentication-token")
  
  return auth_token.text if auth_token is not None else None

class PlexBackend(object):
  
  def authenticate(self, username=None, password=None):

    if username is None or password is None:
      return None

    valid = plex_auth(username, password)
    if valid:
      try:
        user = User.objects.get(username=username)
        user.token = valid
        user.save()
      except User.DoesNotExist:
        # Create a new user. Note that we can set password
        # to anything, because it won't be checked; the password
        # from settings.py will.
        user = User(username=username, password='')
        user.token = valid
        if username in settings.PLEX_ADMIN_USERS:
          user.is_staff = True
          user.is_superuser = True
        user.save()
      return user

    return None

  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None