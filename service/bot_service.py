import configparser
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from entity.user import User
from service import user_service
from states.profile_states import ProfileStates

config = configparser.ConfigParser()
config.read('tg.ini')

bot = Bot(config["tg"]["token"])
dp = Dispatcher(storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


@dp.message(Command('start'))
async def start(message: Message,
                state: FSMContext):
    """
    /start
    If it's new user - save to db and start filling the profile
    """
    await state.clear()

    chat_id: int = message.chat.id
    if not user_service.user_exists(chat_id):
        user: User = User(message.chat.id,
                          'FEMALE',
                          15,
                          message.from_user.username,
                          0,
                          0)
        user_service.create_user(user)
        await fill_profile(message)


async def fill_profile(message: Message):
    """
    Starts the chain of filling the profile
    1) Ask the gender
    2) Ask the age
    3) Ask the name
    """
    man_button = InlineKeyboardButton(text="Я хлопець👨", callback_data="MALE")
    woman_button = InlineKeyboardButton(text="Я дівчинка👩", callback_data="FEMALE")
    keyboard_markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[list([man_button, woman_button])])

    await message.answer(
        text="""Привіт, вітаю тебе в боті анонімного спілкування.
Спершу, напиши свою стать""",
        reply_markup=keyboard_markup)


@dp.callback_query(lambda c: c.data in ['MALE', 'FEMALE'])
async def process_gender_callback(callback_query: CallbackQuery,
                                  state: FSMContext):
    """ Changes the age of user to db, prepare state to change age """
    sex = callback_query.data
    chat_id = callback_query.message.chat.id

    user_service.update_user_sex(sex, chat_id)
    await callback_query.answer()
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)

    await ask_age(callback_query.message, state)


@dp.message(ProfileStates.ask_age)
async def process_ask_age(message: Message,
                          state: FSMContext):
    age = message.text
    try:
        age = int(age)
    except ValueError:
        return await message.answer("Будь ласка введіть Ваш реальний вік")

    user_service.update_user_age(age=age,
                                 chat_id=message.chat.id)
    await ask_name(message, state)


async def ask_age(message: Message,
                  state: FSMContext):
    await message.answer("А тепер введи свій вік")
    await state.set_state(ProfileStates.ask_age)


async def ask_name(message: Message,
                   state: FSMContext):
    await message.answer("Як мені тебе називати?")
    pass


async def init_bot():
    await dp.start_polling(bot)
