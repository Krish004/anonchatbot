from aiogram.fsm.state import StatesGroup, State


class ChatStates(StatesGroup):
    search = State()
    chatting = State()
    reaction = State()
