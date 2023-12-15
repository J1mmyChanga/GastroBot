from aiogram.fsm.state import StatesGroup, State

class CustomMealState(StatesGroup):
    recipe = State()