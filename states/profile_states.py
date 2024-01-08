from aiogram.fsm.state import StatesGroup, State


class ProfileStates(StatesGroup):
    ask_gender = State()
    ask_age = State()
