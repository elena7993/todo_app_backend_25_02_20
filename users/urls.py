from django.urls import path
from .views import Me

urlpatterns = [
    path("me/", Me.as_view()),
]

# MVC = Model view controll
# MVT = Model view template
