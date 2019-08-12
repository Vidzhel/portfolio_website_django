from django.urls import path
from .views import projects

urlpatterns = [
    path("", projects, name="projects_list"),
    path("<slug:filtered>", projects, name="projects_list"),
]
