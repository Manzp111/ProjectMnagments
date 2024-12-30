from  django import  forms
from core.models import Contact_User
from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_User
        fields = ['name', 'email', 'phone_number', 'message']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
