from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("project_list")  # ログイン後のリダイレクト先
    else:
        form = CustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})
