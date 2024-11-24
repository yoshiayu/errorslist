from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import set_language_and_clear_cookie


# URLパターン
urlpatterns = [
    path("admin/", admin.site.urls),  # 管理画面
    path("accounts/", include("users.urls")),  # 認証関連
    path("i18n/", include("django.conf.urls.i18n")),  # 言語切り替え用
    path("errors/", include("errors.urls")),  # errors アプリを登録
    path("custom-setlang/", set_language_and_clear_cookie, name="custom_set_language"),
]


# 言語切り替え用のURLパターン
urlpatterns += i18n_patterns(
    path("projects/", include("projects.urls")),  # プロジェクト関連
    path("", TemplateView.as_view(template_name="base.html"), name="home"),  # ホーム
    prefix_default_language=True,  # デフォルト言語をプレフィックスに含めない
)


# 言語切り替え用のURL
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
