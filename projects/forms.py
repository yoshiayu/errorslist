from django import forms
from .models import UserProject


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
