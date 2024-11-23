import json
import os


def extract_python_errors():
    errors = []
    for error_name in dir(__builtins__):
        error_class = getattr(__builtins__, error_name)
        if isinstance(error_class, type) and issubclass(error_class, BaseException):
            errors.append(
                {
                    "model": "errors.error",
                    "pk": len(errors) + 1,
                    "fields": {
                        "name": error_class.__name__,
                        "description": error_class.__doc__,
                        "solution": "Refer to Python documentation for resolution.",
                        "created_at": "2024-11-22T12:00:00Z",
                        "updated_at": "2024-11-22T12:00:00Z",
                    },
                }
            )
    return errors


if __name__ == "__main__":
    # 保存先ディレクトリ
    output_dir = "errors/fixtures"
    os.makedirs(output_dir, exist_ok=True)

    # エラーリストの抽出
    python_errors = extract_python_errors()

    # JSONファイルへの書き込み
    output_path = os.path.join(output_dir, "python_errors.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(python_errors, f, indent=4, ensure_ascii=False)

    print(f"Python errors have been saved to {output_path}")
