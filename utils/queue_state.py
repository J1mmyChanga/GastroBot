from aiogram import Bot
import requests
from aiogram.utils import markdown

from create_entities import session
from data.user_model import User

async def queue_state(bot: Bot):
    for user in session.query(User).all():
        # states = requests.get('https://signal.umom.pro/get_state').json()
        states = requests.get('http://127.0.0.1:5000/get_state').json()
        # states = requests.get('https://signal-imitator.onrender.com').json()
        print(states)
        new_state_yellow, new_state_red = states.get('new_state_yellow', False), states.get('new_state_red', False)
        old_state_yellow, old_state_red = states.get('old_state_yellow', False), states.get('old_state_red', False)
        text = markdown.text('Очереди практически нет. Можете смело спускаться в столовую!',
                             'Приблизительное время в очереди: меньше 7ми минут.'
                             )
        if new_state_yellow:
            text = markdown.text('Очереди средней длины. Возможно стоит сделать заказ в мобильном приложении.',
                                 'Приблизительное время в очереди: больше 7ми минут.'
                                 )
        if new_state_red:
            text = markdown.text('Очередь очень длинная. Советуем сделать заказ в мобильном приложении.',
                                 'Приблизительное время в очереди: около 15ти минут.'
                                 )
        if (old_state_yellow, old_state_red) != (new_state_yellow, new_state_red) or (new_state_yellow, new_state_red) == (False, False):
            await bot.send_message(chat_id=user.user_id, text=text)