from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from create_entities import dp
from keyboards import *

from states import CustomMealState
from utils import nutrits_counter


@dp.message(F.text.lower().startswith('предложить своё блюдо'))
async def custom_meal_handler(message: types.Message, state: FSMContext):
    await state.set_state(CustomMealState.recipe)
    await message.answer(
        text=markdown.text('- ✍ 🧾 Напишите подробный рецепт вашего блюда и все необходимые ингридиенты. 🥒🥦🧅🫘🥩\n',
                           '- Помните, что ингридиенты должны быть доступными и не из разряда лобстеров и т.д. 🍖 🧀\n',
                           '- 🧾 Ваш рецепт отправиться на модерацию на кухню. Там рассмотрят ваше предложение и если рецепт будет одобрен, то он будет учавствовать в голосвании за добавление блюд в бизнес-ланчи в конце месяца. 📋 📊\n',
                           sep = '\n',
                           )
    )


@dp.message(CustomMealState.recipe)
async def custom_meal_recipe_handler(message: types.Message, state: FSMContext):
    data = await state.update_data(recipe=message.text)
    recipe = data['recipe']
    print(recipe)
    await state.clear()
    data = nutrits_counter(recipe).split('\n')
    try:
        callories = f'- 🥘 {data[0]}'
        fats = f'- 🧀 {data[1]}'
        proteins = f'- 🥩 {data[2]}'
        carbohydrates = f'- 🍔 {data[3]}'
        await message.answer(
            text=markdown.text(
                'КБЖУ вашего блюда на 100 г продукта:',
                f'{callories}',
                f'{fats}',
                f'{proteins}',
                f'{carbohydrates}\n',
                '🥘 Ваше блюдо успешно отправлено на рассмотрение модерации. ✅\n',
                '🧾 Как только ваш рецепт одобрят, вы незамедлительно получить оповещение. 📨\n',
                'Спасибо, что делаете нас лучше! 🙏 🌟\n',
                sep='\n'
            ),
        )
    except Exception:
        callories = f'- 🥘 Калории: не удалось найти'
        fats = f'- 🧀 Жиры: не удалось найти'
        proteins = f'- 🥩 Белки: не удалось найти'
        carbohydrates = f'- 🍔 Углеводы: не удалось найти'
        await message.answer(
            text=markdown.text(
                'КБЖУ вашего блюда на 100 г продукта:',
                f'{callories}',
                f'{fats}',
                f'{proteins}',
                f'{carbohydrates}\n',
                'Похоже что-то пошло не так(. Попробуйте нажать на кнопку предложения блюда и ввести рецепт еще раз. 🧾 ✍\n',
                sep='\n'
            ),
        )