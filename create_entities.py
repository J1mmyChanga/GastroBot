from aiogram import Bot, Dispatcher

from config import settings
from data import *

dp = Dispatcher()
bot = Bot(
    token=settings.bot_token
)

global_init('db/gastro_bot.db')
session = create_session()