from aiogram import Bot, Dispatcher

from config import settings
from data import *
# from middlewares import QueueStateMiddleware

dp = Dispatcher()
#dp.callback_query.middleware(QueueStateMiddleware())
bot = Bot(
    token=settings.bot_token
)
global_init('db/gastro_bot.db')
session = create_session()