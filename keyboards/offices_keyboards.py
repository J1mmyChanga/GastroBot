from aiogram import types


def create_offices_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text='Адрес 1', callback_data=f'office_1')],
        [types.InlineKeyboardButton(text='Адрес 2', callback_data=f'office_2')],
        [types.InlineKeyboardButton(text='Адрес 3', callback_data=f'office_3')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard