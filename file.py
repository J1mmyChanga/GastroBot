from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='N2U0Njg4NzUtNGQxZS00NjZiLThmZGYtYTg1YTk4MjI4YmZlOjdiMjY1M2U0LTAzMDktNDU4My1hNmJhLTZjZTczNzU3N2IwMA==', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]

while(True):
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    print("Bot: ", res.content)