import dotenv
import os

dotenv.load_dotenv()

folder_id = os.getenv("YC_FOLDER_ID")
api_key = os.getenv("YC_API_KEY")

if not folder_id:
    raise RuntimeError("YC_FOLDER_ID не найден!")

if not api_key:
    raise RuntimeError("YC_API_KEY не найден!")

print("Настройки Yandex Cloud успешно загружены!")
