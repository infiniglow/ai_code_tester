from pathlib import Path
from agent.generator import generate_tests

task_description = """
Написать функцию divide(a, b), которая делит число a на число b.
Если b равен нулю, функция должна выбрасывать исключение ZeroDivisionError.
"""

workspace = Path("workspace")
source_code = (workspace / "source.py").read_text(encoding="utf-8")

try:
    tests = generate_tests(task_description, source_code)

    test_file = workspace / "test_generated.py"
    test_file.write_text(tests, encoding="utf-8")

    print("Тесты успешно сохранены!")

except RuntimeError as error:
    print("Не удалось сгенерировать тесты:", error)
