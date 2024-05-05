# csh. 5th May 2024.
# Create this urls.py for every app created by you
from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalog_home, name="Library Home"),

]