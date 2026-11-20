from agent.llm import send_request

prompt = "Привет! Представься и расскажи, что ты умеешь."
answer = send_request(prompt)

print("Ответ языковой модели:", answer, sep="\n")
