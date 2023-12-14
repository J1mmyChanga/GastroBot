from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.enums import ParseMode
from create_entities import *
from misc import *


@dp.message(CommandStart())
async def handle_command_start(message: types.Message):
    text = 'Поздравляем, бот готов к использованию! ✅\nВыберите, что бы хотели сделать: 🔎'
    kb = [
        [types.KeyboardButton(text='Предложить своё блюдо 🍳🥗🥪')],
        [types.KeyboardButton(text='Написать отзыв о бизнес-ланче 📝')],
        [types.KeyboardButton(text='Голос за блюдо в следующем бизнес-ланче 🌯🌭🍕')],
        [types.KeyboardButton(text='Хочу получать оповещения о длине очереди 💬')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Выберите кнопку',
    )
    await message.answer(
        text=text,
        reply_markup=keyboard,
    )
    session.commit()


@dp.message(Command('help'))
async def handle_command_help(message: types.Message):
    text = markdown.text(
        '🌟 ☕ GastroBot - твоя книга отзывов и предложений сервиса "Кейтеринбург" прямо в кармане! 📚 📖\n',
        '🥘 Наскучили бизнес-ланчи - не беда! Просто предложи свой. Если твоё блюдо окажется достаточно вкусным и его оценят другие, то можешь ждать его в гастроемкостях нашей столовой:) 🍱 🫕 \n',
        '✍ Очень понравилось блюдо из бизнес-ланча и хочешь, чтобы об этом знали все? - Напиши свой отзыв на это блюдо прямо в телеграм боте! 📝\n',
        '🗳️ Хотите чаще видеть какое-то блюдо в бизнес-ланчах? - Проголосуйте за него и оно будет чаще появляться на полках нашей столовой!\n',
        '🌱 Оставляя отзывы на наши бизнес-ланчи, голосуя за любимые блюда, и предлагая новые позиции, вы позволяете нам беспрерывно улучшаться и расти в качестве.\n',
        '🙏 Спасибо вам за это! 🌟👏\n',
        sep=' \n '
    )
    await message.answer(
        text=text,
        parse_mode=None,
    )