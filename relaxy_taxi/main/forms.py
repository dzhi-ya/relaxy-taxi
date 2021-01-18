from django import forms

from .models import Order
from ..users.models import User


class CallbackForm(forms.Form):
    name = forms.CharField()
    phone_number = forms.CharField()
    client_comment = forms.CharField(widget=forms.Textarea)

    def save(self, user: User, *args, **kwargs):
        cd = self.cleaned_data

        name = cd["name"]
        phone_number = cd["phone_number"]
        client_comment = cd["client_comment"]

        client = user
        if not client.name:
            client.name = name

        if not client.phone_number:
            client.phone_number = phone_number

        client.save()
        Order.objects.create(
            client=client,
            client_comment=client_comment,
        )
