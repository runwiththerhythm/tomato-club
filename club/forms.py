# club/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your name",
        widget=forms.TextInput(attrs={"placeholder": "Jane Tomato"})
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"})
    )
    subject = forms.CharField(
        max_length=150,
        label="Subject",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Question about membership, seeds, etc."})
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us a bit about your query…"})
    )
