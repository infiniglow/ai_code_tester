from agent.llm import send_request


def generate_tests(task_description, source_code):
    prompt = f"""
Ты — опытный Python-разработчик и специалист по тестированию.
Твоя задача — написать автоматические тесты для предоставленного Python-кода.

Описание задачи:
{task_description}

Исходный код:
{source_code}

Требования:
1. Используй библиотеку pytest.
2. Проверь корректные входные данные.
3. Проверь граничные случаи.
4. Проверь обработку некорректных входных данных.
5. Верни только исполняемый Python-код тестов, без пояснений и Markdown-блоков.
"""

    return send_request(prompt)
