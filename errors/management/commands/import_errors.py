from django.core.management.base import BaseCommand
from errors.models import Error
import json
from pathlib import Path


class Command(BaseCommand):
    help = "Import errors from python_errors.json and extract solutions"

    def handle(self, *args, **kwargs):
        # JSONファイルのパス
        fixture_path = Path("errors/fixtures/python_errors.json")
        if not fixture_path.exists():
            self.stdout.write(self.style.ERROR(f"{fixture_path} does not exist."))
            return

        try:
            with open(fixture_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # データの処理
            for entry in data:
                if "fields" not in entry:
                    self.stdout.write(
                        self.style.WARNING(f"Skipped invalid entry: {entry}")
                    )
                    continue

                fields = entry["fields"]

                # データベースにインポート
                Error.objects.update_or_create(
                    pk=entry["pk"],
                    defaults={
                        "name": fields["name"],
                        "description": fields["description"],
                        "solution": (
                            fields["solution"]
                            if fields["solution"]
                            != "Refer to Python documentation for resolution."
                            else f"Default solution for {fields['name']}"  # デフォルトの解決方法を設定
                        ),
                    },
                )

            # 解決方法を抽出して出力
            self.stdout.write("\n=== Extracted Solutions ===")
            solutions = [
                f"{i+1}. {entry['fields']['name']}\n   解決方法: {entry['fields']['solution']}\n"
                for i, entry in enumerate(data)
                if "fields" in entry and entry["fields"]["solution"]
            ]
            self.stdout.write("\n".join(solutions))

        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f"JSON format error: {e}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Unexpected error: {e}"))
