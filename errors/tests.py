from django.test import TestCase
from django.urls import reverse
from errors.models import Error


class ErrorAppTestCase(TestCase):
    def setUp(self):
        # サンプルデータ作成
        Error.objects.create(
            name="Error 1", description="Description 1", solution="Solution 1"
        )
        Error.objects.create(
            name="Error 2", description="Description 2", solution="Solution 2"
        )

    def test_error_list_view(self):
        response = self.client.get(reverse("errors:error_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Error 1")
        self.assertContains(response, "Error 2")

    def test_search_functionality(self):
        response = self.client.get(reverse("errors:error_list"), {"q": "Error 1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Error 1")
        self.assertNotContains(response, "Error 2")

    def test_pagination(self):
        # 11個のデータを作成してページネーションをテスト
        for i in range(11):
            Error.objects.create(
                name=f"Error {i+3}", description="Test", solution="Test"
            )
        response = self.client.get(reverse("errors:error_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Error 1")  # 最初のページにはあるはず
        self.assertNotContains(response, "Error 11")  # 最初のページにはないはず

        response = self.client.get(reverse("errors:error_list"), {"page": 2})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Error 11")  # 2ページ目にはあるはず

    def test_language_change(self):
        response = self.client.post(
            reverse("errors:set_language_and_clear_cookie"), {"language": "ja"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.cookies["django_language"].value, "ja")

    def test_invalid_language(self):
        response = self.client.post(
            reverse("errors:set_language_and_clear_cookie"), {"language": "invalid"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.client.cookies["django_language"].value, "en"  # デフォルト言語を確認
        )
