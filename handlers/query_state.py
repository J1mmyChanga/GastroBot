from aiogram import types, F
from aiogram.utils import markdown
from create_entities import *
from misc import *


def create_offices_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text='Адрес 1', callback_data=f'office_1')],
        [types.InlineKeyboardButton(text='Адрес 2', callback_data=f'office_2')],
        [types.InlineKeyboardButton(text='Адрес 3', callback_data=f'office_3')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

@dp.message(F.text.lower().startswith('хочу получать оповещения'))
async def office_choice_handler(message: types.Message):
    await message.answer(
        text=markdown.text('Выберите здание, в котором работаете 👨‍💻 :'),
        reply_markup=create_offices_keyboard()
    )


@dp.callback_query(F.data.startswith('office'))
async def query_state_handler(message: types.Message):
    await message.answer(
        text=markdown.text('Теперь вы будете получать уведомления о статусе очереди. ✅')
    )
