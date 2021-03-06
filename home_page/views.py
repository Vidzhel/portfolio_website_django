from django.shortcuts import render, HttpResponse
from contact_form.forms import ContactForm
from contact_form.views import manage_form, send_email
from projects.models import ProjectItem
from about.models import About
import json

# Create your views here.


def home_page(request):
    form = ContactForm(request.POST or None)

    # Get last three projects
    projects = (ProjectItem.objects.all())[:3]

    # get about info
    try:
        about_page = (About.objects.all())[0]
        about = about_page.get_cleaned_data()
    except:
        about = {}

    # Check if it form redirection and send response
    if(request.method == "POST"):
        response = manage_form(request, form, send_email)
        return HttpResponse(json.dumps(response), content_type="application/json")

    context = {
        "form": form,
        "projects": projects,
        "about": about.get("about", ""),
        "about_img": about.get("about_img", ""),
        "developer_skills": about.get("developer_skills", ""),
        "designer_skills": about.get("designer_skills", ""),
    }

    tags = []
    # Get tags
    for i in range(len(projects)):
        tags.append(projects[i].tags.all())

    context["tags"] = tags

    return render(request, "home_page/home_page.html", context)
