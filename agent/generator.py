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
2. Проверяй корректные входные данные.
3. Проверяй граничные случаи.
4. Проверяй обработку некорректных входных данных.
5. Не копируй и не реализуй проверяемые функции.
6. Считай, что исходный код находится в файле source.py.
7. Импортируй необходимые функции из source.py.
8. Верни только исполняемый Python-код тестов, без пояснений и Markdown-блоков.
"""

    response = send_request(prompt).strip()

    if response.startswith("```"):
        lines = response.splitlines()

        lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        response = "\n".join(lines).strip()

    return response
