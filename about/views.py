from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import About

# Create your views here.


def about(request):
    try:
        about_page = (About.objects.all())[0]
    except:
        return HttpResponseRedirect(reverse("home_page"))

    context = about_page.get_cleaned_data()

    # print(context)

    return render(request, "about/about.html", context)
