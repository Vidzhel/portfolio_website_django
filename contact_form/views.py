from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from django.template.defaultfilters import striptags
from django.conf import settings
import json
import smtplib

# Create your views here.


def contact_form(request):
    form = ContactForm(request.POST or None)

    # Check if it form redirection and send response
    if(request.method == "POST"):
        response = manage_form(request, form, send_email)
        return HttpResponse(json.dumps(response), content_type="application/json")

    context = {
        "form": form
    }

    return render(request, "contact_test_form/form_preview.html", context)


def manage_form(request, form, action=None):

    # Validate form and make actions
    if form.is_valid():
        if(action != None):
            action(form.cleaned_data)
        response = {"success": "Thanks for being interested in me"}

    else:
        # Get dictionary with field id and error
        response = {}
        for error in form.errors.items():
            response[error[0]] = str(striptags(error[1]))

    return response


def send_email(data):

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        USER_EMAIL = settings.USER_EMAIL
        USER_PASS = settings.USER_PASS

        smtp.login(USER_EMAIL, USER_PASS)

        print(data, USER_EMAIL, USER_PASS)
        subject = "Form submitted from your website"

        body = "\n\n".join([key+": "+value for key, value in data.items()])

        msg = "Subject: "+subject +"\n\n\n" + body

        smtp.sendmail(USER_EMAIL, USER_EMAIL, msg)