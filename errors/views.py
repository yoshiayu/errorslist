from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Error
from django.utils.safestring import mark_safe
from django.utils.html import escape
import logging

logger = logging.getLogger(__name__)


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
