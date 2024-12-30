from django import forms
from .models import Signup,Contact_User,User
from django.contrib.auth.forms import UserCreationForm
from PropertyApp.models import Property,Tenant,Unit,Landroad,Lease,PropertyImage,MaintenanceRequest
from django.forms import modelformset_factory


class SignupForm(forms.ModelForm):
     class Meta:
        model = Signup
        fields ='__all__'

class Contact_User_form(forms.ModelForm):
    class Meta:
        model=Contact_User
        fields='__all__'


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'first_name', 'last_name','user_type']

class UserFormEdit(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'first_name', 'last_name','user_type']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'# Include all fields or specify which ones to include
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'  # Include all fields or specify which ones to include
class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = '__all__'  # Include all fields or specify which ones to include
class LandroadForm(forms.ModelForm):
    class Meta:
        model = Landroad
        fields = '__all__'  # Include all fields or specify which ones to include

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']  # Only include the image field

PropertyImageFormSet = modelformset_factory(PropertyImage, form=PropertyImageForm, extra=2,max_num=5)

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['description']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username']
