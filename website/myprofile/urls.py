from django.conf.urls import url
from . import views

app_name = "myprofile"
urlpatterns = [
        url(r'^$', views.index, name = "index"),
        url(r'^profile/$', views.profile, name = "profile"),
        url(r'^research/$', views.research, name = "research"),
        url(r'^developer/$', views.developer, name = "developer"),
]


