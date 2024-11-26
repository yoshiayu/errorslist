from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from errors.models import Error
from .models import UserProject
from .forms import AddErrorForm, ErrorResolutionForm, ProjectForm


@login_required
def project_list(request):
    projects = UserProject.objects.filter(
        user=request.user
    )  # ログイン中のユーザーのプロジェクトのみ取得
    return render(request, "projects/project_list.html", {"projects": projects})


@login_required
def project_detail(request, pk):
    # プロジェクトの取得
    project = get_object_or_404(UserProject, pk=pk, user=request.user)

    # フォーム初期化
    error_form = AddErrorForm()
    resolution_form = ErrorResolutionForm(instance=project)

    if "add_error" in request.POST:
        error_form = AddErrorForm(request.POST)
        if error_form.is_valid():
            try:
                # 新しいエラーを保存する際に commit=False を使う
                new_error = error_form.save(commit=False)
                new_error.save()  # プライマリキーを確保する
                project.errors.add(new_error)  # プロジェクトに関連付ける
                messages.success(request, "エラーが追加されました。")
            except IntegrityError as e:
                print(f"エラーの保存中に問題: {e}")  # ログを記録
                messages.error(request, "エラーの追加に失敗しました。")
            return HttpResponseRedirect(reverse("project_detail", args=[pk]))

        elif "update_resolution" in request.POST:
            resolution_form = ErrorResolutionForm(request.POST, instance=project)
            if resolution_form.is_valid():
                resolution_form.save()
                messages.success(request, "解決策が更新されました。")
                return HttpResponseRedirect(reverse("project_detail", args=[pk]))

    # エラー一覧を取得
    errors = project.errors.all()

    return render(
        request,
        "projects/project_detail.html",
        {
            "project": project,
            "error_form": error_form,
            "resolution_form": resolution_form,
            "errors": errors,  # テンプレート用エラーリスト
        },
    )


# @login_required
# def project_detail(request, pk):
#     project = get_object_or_404(UserProject, pk=pk, user=request.user)  # ユーザー確認
#     error_form = AddErrorForm()
#     resolution_form = ErrorResolutionForm(instance=project)

#     if request.method == "POST":
#         if "add_error" in request.POST:
#             error_form = AddErrorForm(request.POST)
#             if error_form.is_valid():
#                 try:
#                     new_error = error_form.save(commit=False)
#                     new_error.save()  # 新しいエラーを保存
#                     project.errors.add(new_error)  # プロジェクトとエラーを関連付け
#                     project.save()  # 変更を確定
#                     messages.success(request, "エラーを正常に追加しました。")
#                 except IntegrityError:
#                     messages.error(
#                         request,
#                         "エラーの追加中に問題が発生しました。同じエラーが既に存在する可能性があります。",
#                     )
#                 return HttpResponseRedirect(reverse("project_detail", args=[pk]))

#         elif "update_resolution" in request.POST:
#             resolution_form = ErrorResolutionForm(request.POST, instance=project)
#             if resolution_form.is_valid():
#                 resolution_form.save()
#                 messages.success(request, "解決策を正常に更新しました。")
#                 return HttpResponseRedirect(reverse("project_detail", args=[pk]))

#     # プロジェクトのエラー一覧を取得してテンプレートに渡す
#     errors = project.errors.all()

#     return render(
#         request,
#         "projects/project_detail.html",
#         {
#             "project": project,
#             "error_form": error_form,
#             "resolution_form": resolution_form,
#             "errors": errors,  # エラーリストを渡す
#         },
#     )


@login_required
def upload_file(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # ログイン中のユーザーを設定
            project.save()
            messages.success(
                request, "新しいプロジェクトを正常にアップロードしました。"
            )
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "projects/upload_file.html", {"form": form})


# def upload_file(request):
#     if request.method == "POST":
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user = request.user  # ユーザーを設定
#             project.save()
#             messages.success(
#                 request, "新しいプロジェクトを正常にアップロードしました。"
#             )
#             return redirect("project_list")
#     else:
#         form = ProjectForm()
#     return render(request, "projects/upload_file.html", {"form": form})


@login_required
def delete_project(request, pk):
    print(f"削除対象のプロジェクトID: {pk}")  # デバッグ用
    project = get_object_or_404(UserProject, pk=pk, user=request.user)  # ユーザー確認
    if request.method == "POST":
        project.delete()
        messages.success(
            request, f"プロジェクト「{project.project_name}」を削除しました。"
        )
        return redirect("project_list")
    return render(request, "projects/confirm_delete.html", {"project": project})
