from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # カスタムユーザーモデルを指定
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]  # 必要なフィールドを指定
