from django.core.management.base import BaseCommand
from errors.models import Error
import json
from pathlib import Path


class Command(BaseCommand):
    help = "Import errors from python_errors.json"

    def handle(self, *args, **kwargs):
        # fixtures フォルダ内の python_errors.json ファイルを指定
        fixture_path = Path("errors/fixtures/python_errors.json")
        if not fixture_path.exists():
            self.stdout.write(self.style.ERROR(f"{fixture_path} does not exist."))
            return

        with open(fixture_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            fields = item["fields"]
            # 重複チェックして、存在しない場合のみ作成
            error, created = Error.objects.get_or_create(
                name=fields["name"],
                defaults={
                    "description": fields["description"],
                    "solution": fields["solution"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added error: {error.name}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Skipped existing error: {error.name}")
                )
