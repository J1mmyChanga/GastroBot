from aiogram.fsm.state import StatesGroup, State

class ReviewState(StatesGroup):
    lunch = State()
    review = State()