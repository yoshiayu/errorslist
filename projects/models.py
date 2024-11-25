from django.db import models
from users.models import User
from errors.models import Error  # 正しいモジュールからインポート
from django.utils.translation import gettext_lazy as _


class ProjectDescription(models.Model):
    project = models.ForeignKey(
        "UserProject", on_delete=models.CASCADE, related_name="descriptions"
    )
    description = models.TextField()

    def __str__(self):
        return f"Description for {self.project.project_name}: {self.description[:50]}"


class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    project_name = models.CharField(_("Project Name"), max_length=255)
    project_description = models.TextField(_("Description"))
    uploaded_file = models.FileField(
        _("Uploaded File"), upload_to="uploads/", blank=True, null=True
    )
    errors = models.ManyToManyField(Error, blank=True, related_name="projects")
    error_resolution = models.TextField(_("Error Resolution"), blank=True, null=True)

    def __str__(self):
        return self.project_name


# from django.db import models
# from users.models import User
# from errors.models import Error
# from django.core.files.storage import FileSystemStorage
# from django.utils.translation import gettext_lazy as _
# from django.db import models


# class Project(models.Model):
#     project_name = models.CharField(
#         _("Project Name"), max_length=255
#     )  # 翻訳可能なラベル
#     project_description = models.TextField(_("Description"))  # 翻訳可能なラベル
#     error_resolution = models.TextField(
#         _("Error Resolution"), blank=True, null=True
#     )  # 翻訳可能なラベル
#     uploaded_file = models.FileField(
#         _("Uploaded File"), upload_to="uploads/", blank=True, null=True
#     )  # 翻訳可能なラベル

#     @property
#     def translated_description(self):
#         # 翻訳された説明を返す
#         return _(self.project_description)


# class ProjectDescription(models.Model):
#     project = models.ForeignKey(
#         "UserProject", on_delete=models.CASCADE, related_name="descriptions"
#     )
#     description = models.TextField(_("Description"))

#     def __str__(self):
#         return f"Description for {self.project.project_name}: {self.description[:50]}"


# class UserProject(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
#     project_name = models.CharField(_("Project Name"), max_length=255)
#     project_description = models.TextField(_("Description"), blank=True, null=True)
#     uploaded_file = models.FileField(
#         _("Uploaded File"), upload_to="uploads/", blank=True, null=True
#     )
#     errors = models.ManyToManyField("errors.Error", blank=True, related_name="projects")
#     error_resolution = models.TextField(_("Error Resolution"), blank=True, null=True)

#     def __str__(self):
#         return self.project_name


# class UserProject(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
#     project_name = models.CharField(_("Project Name"), max_length=255)
#     # project_name = models.CharField(max_length=255)
#     project_description = models.TextField(_("Description"))
#     # project_description = models.TextField(blank=True, null=True)
#     project_file = models.JSONField(blank=True, null=True)  # 空の値を許可
#     error_log = models.JSONField(blank=True, null=True)
#     errors = models.ManyToManyField(Error, blank=True)
#     uploaded_file = models.FileField(
#         _("Uploaded File"), upload_to="uploads/", blank=True, null=True
#     )
#     # uploaded_file = models.FileField(upload_to="uploads/", storage=FileSystemStorage(), blank=True, null=True)
#     error_resolution = models.TextField(_("Error Resolution"), blank=True, null=True)
#     # error_resolution = models.TextField(null=True, blank=True)  # エラー対処方法の記録

#     def __str__(self):
#         return self.project_name
