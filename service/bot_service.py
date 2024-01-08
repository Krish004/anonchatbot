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
                          '',
                          message.from_user.username,
                          0,
                          0)
        user_service.create_user(user)
        await message.answer("Привіт, вітаю тебе в боті анонімного спілкування.")
        await fill_profile(message)
    else:
        await send_user_profile(message)


async def fill_profile(message: Message):
    """
    Starts the chain of filling the profile
    1) Asks the gender
    2) Asks the age
    3) Asks the name
    """
    man_button = InlineKeyboardButton(text="Я хлопець👨", callback_data="MALE")
    woman_button = InlineKeyboardButton(text="Я дівчинка👩", callback_data="FEMALE")
    keyboard_markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=[list([man_button, woman_button])])

    await message.answer(
        text="Вибери свою стать",
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


async def ask_age(message: Message,
                  state: FSMContext):
    await message.answer("Введи свій вік")
    await state.set_state(ProfileStates.ask_age)


@dp.message(ProfileStates.ask_age)
async def process_ask_age(message: Message,
                          state: FSMContext):
    age = message.text
    try:
        age = int(age)
        if age < 0 or age > 100:
            raise ValueError("Вибраний вік поза межами")
    except ValueError:
        return await message.answer("Будь ласка введіть Ваш реальний вік")

    user_service.update_user_age(age=age,
                                 chat_id=message.chat.id)
    await ask_name(message, state)


async def ask_name(message: Message,
                   state: FSMContext):
    await message.answer("Як мені тебе називати?")
    await state.set_state(ProfileStates.ask_name)


@dp.message(ProfileStates.ask_name)
async def process_ask_name(message: Message,
                           state: FSMContext):
    name: str = message.text
    user_service.update_user_name(name, message.chat.id)
    await state.clear()
    await send_user_profile(message)


async def send_user_profile(message: Message):
    user: User = user_service.get_user_by_chat_id(message.chat.id)

    fill_profile_button = InlineKeyboardButton(text="Заповинти профіль наново", callback_data="profile")
    markup = InlineKeyboardMarkup(inline_keyboard=[[fill_profile_button]])

    await message.answer(text=user.get_profile(),
                         reply_markup=markup)


@dp.callback_query(lambda c: c.data == 'profile')
async def send_profile(callback_query: CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await fill_profile(callback_query.message)


async def init_bot():
    await dp.start_polling(bot)
