from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.utils.translation import activate
import logging

logger = logging.getLogger(__name__)


# カスタム言語切り替え
def set_language_and_clear_cookie(request):
    language_code = request.POST.get("language")
    if language_code not in ["en", "ja"]:  # 安全対策: 許可されていない言語をブロック
        language_code = "ja"
    response = HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    response.delete_cookie("django_language")  # クッキーを削除
    response.set_cookie("django_language", language_code)  # 新しいクッキーを設定
    activate(language_code)
    return response


# URLパターン
urlpatterns = [
    path("admin/", admin.site.urls),  # 管理画面
    path("accounts/", include("users.urls")),  # 認証関連
    path("i18n/", include("django.conf.urls.i18n")),  # 言語切り替え用
    path("errors/", include("errors.urls")),  # errors アプリを登録
]


# 言語切り替え用のURLパターン
urlpatterns += i18n_patterns(
    path("projects/", include("projects.urls")),  # プロジェクト関連
    path("", TemplateView.as_view(template_name="base.html"), name="home"),  # ホーム
    prefix_default_language=False,  # デフォルト言語をプレフィックスに含めない
)


# 言語切り替え用のURL
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
