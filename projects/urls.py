from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),  # プロジェクト一覧
    path("<int:pk>/", views.project_detail, name="project_detail"),  # プロジェクト詳細
    path("upload/", views.upload_file, name="upload_file"),  # プロジェクトアップロード
    path(
        "delete/<int:pk>/", views.delete_project, name="delete_project"
    ),  # プロジェクト削除
]
