from django.shortcuts import render, HttpResponse
from contact_form.forms import ContactForm
from contact_form.views import manage_form, send_email
from projects.models import ProjectItem
import json

# Create your views here.


def home_page(request):
    form = ContactForm(request.POST or None)

    # Get last three projects
    projects = (ProjectItem.objects.all())[:3]

    # Check if it form redirection and send response
    if(request.method == "POST"):
        response = manage_form(request, form, send_email)
        return HttpResponse(json.dumps(response), content_type="application/json")

    context = {
        "form": form,
        "projects": projects
    }

    tags = []
    # Get tags
    for i in range(len(projects)):
        tags.append(projects[i].tags.all())

    context["tags"] = tags

    return render(request, "home_page/home_page.html", context)
