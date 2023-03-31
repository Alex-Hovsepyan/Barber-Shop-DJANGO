from django import forms
from .models import BookaSeatContact

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = BookaSeatContact
        fields = ['user_name', 'user_phone', 'user_time', 'user_place', 'user_date', 'user_text']