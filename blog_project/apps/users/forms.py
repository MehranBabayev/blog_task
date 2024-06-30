from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("name", "surname", "email", "password1", "password2")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("name", "surname", "email")
