from agent.generator import generate_tests

task_description = """
Написать функцию divide(a, b), которая делит число a на число b.
Если b равен нулю, функция должна выбрасывать исключение ZeroDivisionError.
"""

source_code = """
def divide(a, b):
    return a / b
"""

try:
    tests = generate_tests(task_description, source_code)
    print("Сгенерированные тесты:", tests, sep="\n")

except RuntimeError as error:
    print("Не удалось сгенерировать тесты:", error)
