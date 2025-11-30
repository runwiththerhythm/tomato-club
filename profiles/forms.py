# profiles/forms.py
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "display_name",
            "location",
            "favourite_tomato",
            "avatar",
        ]
        widgets = {
            "display_name": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "location": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "favourite_tomato": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        }
