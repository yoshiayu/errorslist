from django.test import TestCase
from django.urls import reverse
from .models import Error


class ErrorListViewTests(TestCase):
    def setUp(self):
        Error.objects.create(
            name="ModuleNotFoundError",
            description="指定されたモジュールが見つかりません。",
            solution="pip install で必要なモジュールをインストールしてください。",
        )
        Error.objects.create(
            name="IndentationError",
            description="インデントが正しくありません。",
            solution="インデントを正しく修正してください。",
        )

    def test_search_results(self):
        response = self.client.get(reverse("error_list"), {"q": "IndentationError"})
        self.assertContains(response, "IndentationError")
        self.assertNotContains(response, "ModuleNotFoundError")
