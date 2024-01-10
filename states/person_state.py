from aiogram.fsm.state import StatesGroup, State


class PersonState(StatesGroup):
    contact = State()
