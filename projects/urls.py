from django.urls import path
from .views import projects, project_details

urlpatterns = [
    path("", projects, name="projects_list"),
    path("<slug:filtered>", projects, name="projects_list_filtered"),
    path("details/<slug:alias>", project_details, name="project_details"),
]
