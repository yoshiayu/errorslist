from django.core.management.base import BaseCommand
from projects.models import Project


class Command(BaseCommand):
    help = "テスト用プロジェクトデータを作成します。"

    def handle(self, *args, **kwargs):
        Project.objects.create(
            project_name="テストプロジェクト",
            project_description="これはテスト用のプロジェクトです。",
        )
        self.stdout.write(self.style.SUCCESS("テストデータを作成しました！"))
