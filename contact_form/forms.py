from django import forms


class ContactForm(forms.Form):
    """Represent contact form on the main page that will send message on my email"""

    sender_name = forms.CharField(max_length=20, label="",
                                  widget=forms.TextInput(attrs={"placeholder": "Your Name",
                                                                "id": "sender_name"}))
    sender_email = forms.EmailField(max_length=40, label="",
                                    widget=forms.EmailInput(attrs={"placeholder": "Your Email",
                                                                   "id": "sender_email"}))
    subject = forms.CharField(max_length=40, label="",
                              widget=forms.TextInput(attrs={"placeholder": "Subject",
                                                            "id": "subject"}))
    sender_message = forms.CharField(label="",
                                     widget=forms.Textarea(attrs={"placeholder": "Your Message",
                                                                  "id": "sender_message",
                                                                  "rows": "10"}))
