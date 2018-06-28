from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home')
]

# On the top line we import path from Django to power our urlpattern and on the next line we import our views. The period used here from . import views means reference the current directory, which is our pages app containing both views.py and urls.py. Our urlpattern has three parts: a Python regular expression for the empty string '', specify the view which is called homePageView, add an optional url name of 'home'. In other words, if the user requests the homepage, represented by the empty string '' then use the view called homePageView.