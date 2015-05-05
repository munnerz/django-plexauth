from django.conf.urls import patterns, url

from .views import login_user, logout_user

urlpatterns = patterns('',
    (r'^login/?', login_user),
    (r'^logout/?', logout_user),
)