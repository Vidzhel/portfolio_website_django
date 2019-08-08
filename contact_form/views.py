from django.shortcuts import render, HttpResponse
from .forms import ContactForm
import json
from django.template.defaultfilters import striptags

# Create your views here.


def contact_form(request):
    form = ContactForm(request.POST or None)

    # Check if it form redirection
    if(request.method == "POST"):
        # Validate form and make actions

        if form.is_valid():
            send_email(form.cleaned_data)
            form = ContactForm()
            response = {"success": "Thanks for being interested in me"}

        else:
            # Get dictionary with field id and error
            response = {}
            for error in form.errors.items():
                response[error[0]] = str(striptags(error[1]))

        return HttpResponse(json.dumps(response), content_type="application/json")

    context = {
        "form": form
    }

    return render(request, "contact_test_form/form_preview.html", context)


def send_email(data):
    print("data")
    print(data)
