from django import forms
from .models import NewsletterSubscriber



BASE_INPUT_CLASSES = (
    "input input-bordered w-full "
    "border border-base-300 "
    "focus:border-primary focus:ring-primary/20"
)

BASE_TEXTAREA_CLASSES = (
    "textarea textarea-bordered w-full "
    "border border-base-300 "
    "focus:border-primary focus:ring-primary/20"
)


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Jane Tomato",
                "class": BASE_INPUT_CLASSES,
            }
        ),
    )

    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "class": BASE_INPUT_CLASSES,
            }
        ),
    )

    subject = forms.CharField(
        max_length=150,
        label="Subject",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Question about membership, seeds, etc.",
                "class": BASE_INPUT_CLASSES,
            }
        ),
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "placeholder": "Tell us a bit about your query…",
                "class": BASE_TEXTAREA_CLASSES,
            }
        ),
    )


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if NewsletterSubscriber.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("You’re already subscribed with this email.")
        return email