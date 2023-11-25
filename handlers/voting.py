from aiogram import F
from create_entities import *
from aiogram.utils import markdown
from misc import *


@dp.message(F.text.lower().startswith('голос за блюдо в следующем бизнес'))
async def voting_handler(message: types.Message):
    await message.answer(
        text='📊 Вы можете выбрать блюдо, которое будет в бизнес-ланче на следующей неделе:',
        reply_markup=create_voting_keyboard()
    )


@dp.callback_query(F.data.startswith('vote_'))
async def choose_lunch_voting_handler(callback: types.CallbackQuery):
    session = create_session()
    id = callback.data.split('_')[-1]
    # param = session.get(AdviceParams, id).param
    # advices = [i.advice for i in session.query(Advices).filter(Advices.param == id)]
    await callback.message.answer(
        text=markdown.text(
            'Большое спасибо за ваш голос! 🙏',
            'Он обязательно будет учтен в составлении следующих бизнес-ланчей. 🌟',
            sep='\n'
        ),
    )