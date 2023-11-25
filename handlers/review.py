from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils import markdown
from create_entities import *
from misc import *


class ReviewState(StatesGroup):
    lunch = State()
    review = State()


@dp.message(F.text.lower().startswith('написать отзыв о бизнес-ланче'))
async def choose_lunch_review_handler(message: types.Message, state: FSMContext):
    await state.set_state(ReviewState.lunch)
    await message.answer(
        text='🥘 Выберите бизенс-ланч, для которого вы хотели бы написать отзыв ✍ 📝:',
        reply_markup=create_review_keyboard()
    )


@dp.callback_query(F.data.startswith('rev_'), ReviewState.lunch)
async def input_review_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(lunch=callback.data.split('_')[-1])
    await state.set_state(ReviewState.review)
    await callback.message.answer(
        text=markdown.text(
            '✍ Напишите ваш отзыв: ',
        )
    )


@dp.message(ReviewState.review)
async def review_handler(message: types.Message, state: FSMContext):
    data = await state.update_data(review=message.text)
    review, lunch = data['review'], data['lunch']
    print(review, lunch)
    await state.clear()
    await message.answer(
        text=markdown.text(
            'Ваш отзыв получен! ✅',
            'Теперь все смогут понять, насколько вкусное это блюдо) 🍱',
            'Спасибо, что делаете нас лучше! 🙏 🌟',
            sep='\n'
        )
    )
