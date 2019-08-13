from django.shortcuts import render, HttpResponse
from .models import ProjectItem, Tag, Category
from django.core.serializers.json import DjangoJSONEncoder
import json
import operator

PAGINATION_PAGE_NUM = 5

# Create your views here.

def filter_projects(request, is_json=False):

    # Try to get tags and category form the GET request
    if(is_json):
        tags_regex = ""
        category = "all"

        if(request.GET.get("tags", "") != ""):
            tags = json.loads(request.GET.get("tags", ""))
            tags_regex = "^(" + \
                "|".join(tags) + ")$"
        
        if(request.GET.get("category", "") != ""):
            category = json.loads(request.GET.get("category", ""))
    else:
        tags = request.GET.get("tags", "")
        tags_regex = "^(" + tags + ")$"
        category = request.GET.get("category", "all")
    
    # Num of page (for pagination)
    page = int( request.GET.get("page", "0"))
    
    # Get centain objects from db
    if(category.lower() == "all" and len(tags) == 0):
        projects = ProjectItem.objects.all().distinct()
    elif(category.lower() == "all"):
        projects = ProjectItem.objects.filter(
            tags__name__iregex=tags_regex).distinct()
    elif(len(tags) != 0):
        projects = ProjectItem.objects.filter(
            tags__name__iregex=tags_regex, categories__name__iexact=category).distinct()
    else:
        projects = ProjectItem.objects.filter(
            categories__name__iexact=category).distinct()

    # Return set of unique projects regarding to the page, activated tags,
    #  categoires and overall count of projects
    # First project included, last excluded
    first_project = PAGINATION_PAGE_NUM * page 
    last_project = PAGINATION_PAGE_NUM + page * PAGINATION_PAGE_NUM
    print(projects)
    return (projects[first_project:last_project], tags, category, len(projects))


def projects(request, filtered=""):

    if(filtered.lower() == "filtered" and request.GET):
        filtered_data = filter_projects(request)
        filtered_projects = filtered_data[0]
        activated_tag = Tag.objects.filter(name__iexact="".join(filtered_data[1]))
        activated_category = Tag.objects.filter(name__iexact="".join(filtered_data[2]))
        
        categories = Category.objects.all()
        tags = Tag.objects.all()

        context = {
            "categories": categories,
            "activated_tag": activated_tag,
            "activated_category": activated_category,
            "tags": tags,
            "projects": filtered_projects,
            "projects_count": filtered_data[3]
        }

        return render(request, "projects/portfolio.html", context)


    # Response to the client filter request
    elif(request.GET):
            
        # Prepare project to send them back
        projects_data = []
        filtered_data = filter_projects(request, True)
        projects = filtered_data[0]
        projects_count = filtered_data[3]

        for project in projects:

            info = {
                "title": project.title,
                "absolute_url": project.get_absolute_url(),
                "img": "/media/" + str(project.img),
                "description": project.description,
                "tags": list(project.tags.all().values_list("name")),
                "code_source": project.code_source,
                "in_progress": project.in_progress,
                "projects_count": projects_count
            }
            projects_data.append(info)

        return HttpResponse(json.dumps(projects_data))

    # Get all projects, tags and categories
    categories = Category.objects.all()
    tags = Tag.objects.all()
    projects_set = ProjectItem.objects.all().order_by("-upload_date")

    context = {
        "categories": categories,
        "tags": tags,
        "projects": projects_set[0: PAGINATION_PAGE_NUM],
        "projects_count": len(projects_set)
    }

    return render(request, "projects/portfolio.html", context)
