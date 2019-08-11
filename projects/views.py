from django.shortcuts import render, HttpResponse
from .models import ProjectItem, Tag, Category
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.


def projects(request):

    # Response to the client filter request
    if(request.GET):
        print(request.GET)
        try:
            tags = json.loads(request.GET["tags"])
            tags_regex = "^(" + \
                "|".join(tags) + ")$"
            category = json.loads(request.GET["category"])

            if(category.lower() == "all" and len(tags) == 0):
                projects = ProjectItem.objects.all().order_by("-upload_date")
            elif(category.lower() == "all"):
                projects = ProjectItem.objects.filter(
                    tags__name__iregex=tags_regex).order_by("-upload_date")
            elif(len(tags) != 0):
                projects = ProjectItem.objects.filter(
                    tags__name__iregex=tags_regex, categories__name__iexact=category).order_by("-upload_date")
            else:
                projects = ProjectItem.objects.filter(
                    categories__name__iexact=category).order_by("-upload_date")

            print(set(projects))
            projects_data = []
            for project in set(projects):

                info = {
                    "title": project.title,
                    "absolute_url": project.get_absolute_url(),
                    "img": "/media/" + str(project.img),
                    "about": project.about,
                    "tags": list(project.tags.all().values_list("name")),
                    "code_source": project.code_source,
                    "in_progress": project.in_progress,
                }
                projects_data.append(info)

            return HttpResponse(json.dumps(projects_data))
        except KeyError as identifier:
            print(str(identifier))
            print(tags_regex, category)

    # Get all projects, tags and categories
    categories = Category.objects.all()
    tags_regex = Tag.objects.all()
    projects_set = ProjectItem.objects.all()

    context = {
        "categories": categories,
        "tags": tags_regex,
        "projects": projects_set
    }

    return render(request, "projects/portfolio.html", context)
