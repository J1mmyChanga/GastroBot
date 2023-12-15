from aiogram import Bot

from create_entities import session
from data.user_model import User

async def queue_state(bot: Bot):
    for user in session.query(User).all():
        await bot.send_message(chat_id=user.user_id, text='абобабаа')