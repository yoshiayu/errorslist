from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", login_required(views.project_list), name="project_list"),
    path("<int:pk>/", login_required(views.project_detail), name="project_detail"),
    path(
        "upload/", login_required(views.upload_file), name="upload_file"
    ),  # ファイルアップロードURL
]
