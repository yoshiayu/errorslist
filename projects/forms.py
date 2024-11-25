from django import forms
from errors.models import Error
from .models import UserProject, ProjectDescription


class ProjectDescriptionForm(forms.ModelForm):
    class Meta:
        model = ProjectDescription
        fields = ["description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 50}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = UserProject
        fields = ["project_name", "project_description", "uploaded_file"]


class ErrorResolutionForm(forms.ModelForm):
    class Meta:
        model = UserProject
        fields = ["error_resolution"]  # エラー対処方法だけを編集可能に
        widgets = {
            "error_resolution": forms.Textarea(attrs={"rows": 4, "cols": 50}),
        }


class AddErrorForm(forms.ModelForm):
    class Meta:
        model = Error
        fields = ["description", "solution"]  # エラー情報を追加できる
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 50}),
            "solution": forms.Textarea(attrs={"rows": 2, "cols": 50}),
        }
