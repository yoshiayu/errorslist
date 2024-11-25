from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from errors.models import Error  # 修正ポイント
from .models import UserProject
from .forms import AddErrorForm, ErrorResolutionForm


@login_required
def project_list(request):
    projects = UserProject.objects.filter(
        user=request.user
    )  # ログイン中のユーザーのプロジェクトのみ取得
    return render(request, "projects/project_list.html", {"projects": projects})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(UserProject, pk=pk)
    error_form = AddErrorForm()
    resolution_form = ErrorResolutionForm(instance=project)

    if request.method == "POST":
        if "add_error" in request.POST:
            error_form = AddErrorForm(request.POST)
            if error_form.is_valid():
                new_error = error_form.save()
                project.errors.add(new_error)
                return HttpResponseRedirect(reverse("project_detail", args=[pk]))
        elif "update_resolution" in request.POST:
            resolution_form = ErrorResolutionForm(request.POST, instance=project)
            if resolution_form.is_valid():
                resolution_form.save()
                return HttpResponseRedirect(reverse("project_detail", args=[pk]))

    return render(
        request,
        "projects/project_detail.html",
        {
            "project": project,
            "error_form": error_form,
            "resolution_form": resolution_form,
        },
    )


# @login_required
# def project_detail(request, pk):
#     project = get_object_or_404(UserProject, pk=pk)

#     if request.method == "POST":
#         form = ErrorResolutionForm(request.POST, instance=project)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("project_detail", args=[pk]))
#     else:
#         form = ErrorResolutionForm(instance=project)

#     return render(
#         request,
#         "projects/project_detail.html",
#         {
#             "project": project,
#             "form": form,
#         },
#     )


def upload_file(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # ユーザーを設定
            project.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "projects/upload_file.html", {"form": form})
