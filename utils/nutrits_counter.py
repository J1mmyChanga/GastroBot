from langchain.chat_models import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from config import settings

chat = GigaChat(
    credentials=settings.gigachat_token,
    verify_ssl_certs=False,
)

def nutrits_counter(recipe):
    messages = [
        SystemMessage(
            content="Ты ассистент-нутрициолог, который может считать и выдавать калории, белки, жиры и углеводы на 100 грамм блюда по его названию или рецепту. Если не удается узнать эти данные, напиши что не удалось их найти."
        ),
        HumanMessage(content=f"Рассчитай калориии, жиры, белки и угеводы для 100 грамм этого блюда. {recipe}."),
    ]
    try:
        data = chat(messages).content
    except Exception:
        data = nutrits_counter(recipe)
    return data