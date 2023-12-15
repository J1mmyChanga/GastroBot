from aiogram import F
from aiogram.utils import markdown
from create_entities import *
from data.user_model import User
from keyboards import *

@dp.message(F.text.lower().startswith('хочу получать оповещения'))
async def office_choice_handler(message: types.Message):
    await message.answer(
        text=markdown.text('Выберите здание, в котором работаете 👨‍💻 :'),
        reply_markup=create_offices_keyboard()
    )


@dp.callback_query(F.data.startswith('office'))
async def queue_state_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if not session.query(User).filter(User.user_id==user_id).all():
        session.add(User(user_id=user_id))
        session.commit()
    await callback.message.answer(
        text=markdown.text('Теперь вы будете получать уведомления о статусе очереди. ✅')
    )
    session.close()

