from langchain.chat_models import GigaChat
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage


chat = GigaChat(credentials='N2U0Njg4NzUtNGQxZS00NjZiLThmZGYtYTg1YTk4MjI4YmZlOjdiMjY1M2U0LTAzMDktNDU4My1hNmJhLTZjZTczNzU3N2IwMA==', verify_ssl_certs=False, )

messages = [
    SystemMessage(
        content="Ты ассистент-нутрициолог, который может считать и выдавать калории жиры белки и углеводы на 100 грамм блюда по его названию или рецепту."
    ),
    HumanMessage(content="Рассчитай калориии, жиры, белки и угеводы для 100 грамм этого блюда. Овощное рагу."),
]
def f():
    print(chat(messages).content)


flag = True
f()
# try:
#     while flag:
#         f()
#         flag = False
# except Exception:
#     f()