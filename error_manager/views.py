import logging
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.conf import settings

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
