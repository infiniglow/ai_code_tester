from os import getenv
from dotenv import load_dotenv
from openai import OpenAI, APIError

load_dotenv()

YANDEX_FOLDER_ID = getenv("YC_FOLDER_ID")
YANDEX_API_KEY = getenv("YC_API_KEY")

if not YANDEX_FOLDER_ID:
    raise RuntimeError("YC_FOLDER_ID не найден!")

if not YANDEX_API_KEY:
    raise RuntimeError("YC_API_KEY не найден!")

client = OpenAI(
    api_key=YANDEX_API_KEY,
    project=YANDEX_FOLDER_ID,
    base_url="https://ai.api.cloud.yandex.net/v1"
)

MODEL = f"gpt://{YANDEX_FOLDER_ID}/yandexgpt-lite/latest"


def send_request(prompt):
    try:
        response = client.responses.create(
            model=MODEL,
            input=prompt
        )

        return response.output_text

    except APIError as error:
        raise RuntimeError(
            "Ошибка при обращении к Yandex AI API"
        ) from error
