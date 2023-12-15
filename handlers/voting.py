from aiogram import F

from create_entities import *
from aiogram.utils import markdown
from keyboards import *


@dp.message(F.text.lower().startswith('голос за блюдо в следующем бизнес'))
async def voting_handler(message: types.Message):
    await message.answer(
        text='📊 Вы можете выбрать блюдо, которое будет в бизнес-ланче на следующей неделе:',
        reply_markup=create_voting_keyboard()
    )


@dp.callback_query(F.data.startswith('vote_'))
async def choose_lunch_voting_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        text=markdown.text(
            'Большое спасибо за ваш голос! 🙏',
            'Он обязательно будет учтен в составлении следующих бизнес-ланчей. 🌟',
            sep='\n'
        ),
    )