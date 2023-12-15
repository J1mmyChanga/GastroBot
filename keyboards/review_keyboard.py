from aiogram import types
from data import *


def create_review_keyboard():
    # берет все бизнес ланчи - текущей недели
    session = create_session()
    # locations = [(i.location, i.id) for i in session.query(Locations).all()]
    # buttons = [[types.InlineKeyboardButton(text=i[0], callback_data=f'loc_{i[1]}')] for i in locations]
    buttons = [
        [types.InlineKeyboardButton(text='Омлет с сосисками', callback_data=f'rev_1')],
        [types.InlineKeyboardButton(text='Каша молочная 3 злака', callback_data=f'rev_2')],
        [types.InlineKeyboardButton(text='Пудинг с бананом', callback_data=f'rev_3')],
        [types.InlineKeyboardButton(text='Драники с зеленью', callback_data=f'rev_4')],
        [types.InlineKeyboardButton(text='Картофель жареный с грибами', callback_data=f'rev_5')],
        [types.InlineKeyboardButton(text='Тыква запеченая с розмарином', callback_data=f'rev_6')],
        [types.InlineKeyboardButton(text='Рагу овощное', callback_data=f'rev_7')],
        [types.InlineKeyboardButton(text='Борщ сибирский', callback_data=f'rev_8')],
        [types.InlineKeyboardButton(text='Суп Палиц', callback_data=f'rev_9')],
        [types.InlineKeyboardButton(text='Свинина по-французски', callback_data=f'rev_10')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
