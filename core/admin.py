from django.contrib import admin
from  core.models import Signup,Contact_User,User

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'password','username')

@admin.register(Contact_User)
class Contact_UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','message','created_at')
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'password','is_superuser','is_staff','is_active')

# Register your models here.
