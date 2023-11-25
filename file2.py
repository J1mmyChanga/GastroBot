from langchain.chat_models import GigaChat
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = GigaChat(credentials='N2U0Njg4NzUtNGQxZS00NjZiLThmZGYtYTg1YTk4MjI4YmZlOjdiMjY1M2U0LTAzMDktNDU4My1hNmJhLTZjZTczNzU3N2IwMA==', verify_ssl_certs=False, )

template = "Ты полезный ассистент, который умеет переводить {input_language} на {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

# get a chat completion from the formatted messages
print(chat(
    chat_prompt.format_prompt(
        input_language="английский",
        output_language="русский",
        text="Translate this sentense. I love programming.",
    ).to_messages()
).content)