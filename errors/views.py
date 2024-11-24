from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Error
from django.utils.safestring import mark_safe
from django.utils.html import escape
import logging
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import activate

logger = logging.getLogger(__name__)


def set_language_and_clear_cookie(request):
    language_code = request.POST.get("language", settings.LANGUAGE_CODE)
    logger.debug(f"Requested language: {language_code}")

    # 言語が有効か確認
    if language_code not in dict(settings.LANGUAGES).keys():
        logger.error(f"Invalid language code: {language_code}")
        language_code = settings.LANGUAGE_CODE

    response = HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    response.delete_cookie("django_language")
    response.set_cookie("django_language", language_code)
    activate(language_code)

    # クッキーとアクティベーションのログ出力
    logger.debug(f"django_language cookie set to: {language_code}")
    logger.debug(f"Activated language: {language_code}")

    return response


def error_list(request):
    query = request.GET.get("q", "")
    errors = (
        Error.objects.filter(name__icontains=query) if query else Error.objects.all()
    )

    # デバッグログを出力
    logger.debug(f"Query: {query}")
    logger.debug(f"Errors: {list(errors.values())}")

    # ハイライト処理
    if query:
        query = escape(query)
        for error in errors:
            error.description = mark_safe(
                error.description.replace(
                    query, f"<span class='highlight'>{query}</span>"
                )
            )

    # ページネーションの設定 (1ページに10件)
    paginator = Paginator(errors, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "errors/error_list.html", {"page_obj": page_obj, "query": query}
    )


def error_list_view(request):
    query = request.GET.get("q", "")
    errors = (
        Error.objects.filter(name__icontains=query) if query else Error.objects.all()
    )

    # ページネーション
    paginator = Paginator(errors, 10)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    # メッセージのテスト
    from django.contrib import messages

    messages.add_message(request, messages.INFO, "This is a test message.")

    return render(
        request,
        "errors/error_list.html",
        {
            "query": query,
            "page_obj": page_obj,
        },
    )
