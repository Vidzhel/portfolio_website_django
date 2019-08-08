from django.shortcuts import render, HttpResponse
from .forms import ContactForm
import json

# Create your views here.


def contact_form(request):
    print(request.POST)
    form = ContactForm(request.POST or None)

    # Check if it form redirection
    if(request.method == "POST"):
        # Validate form and make actions
        if form.is_valid():
            form = ContactForm()
            send_email(form.changed_data)

        return HttpResponse(json.dumps("form.changed_data"), content_type="application/json")

    context = {
        "form": form
    }

    return render(request, "contact_test_form/form_preview.html", context)


def send_email(data):
    print("data")
    print(data)
