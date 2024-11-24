from aiogram import Bot, Dispatcher, executor, types 
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage= MemoryStorage())


class UserState(StatesGroup):
    # adress = State()
    age = State()
    growth = State()
    weight = State()
    
@dp.message_handler(text = "Рассчитать")
async def buy(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()
    
@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()
    
@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    weight = float(data['weight'])
    growth = float(data['growth'])
    age = float(data['age'])
    # print(f'вес: {weight}, рост: {growth}, возраст: {age}')    
    colories = (10 * weight + 6.25 * growth - 5 * age)
    
    colories_men = colories + 5
    colories_women = colories - 161
    # print(colories_men)
    await message.answer(f'Ваша норма калорий: {colories_men}')
    await state.finish()
    
    
# @dp.message_handler(text = ['Urban', 'ff']) 
# async def urban_message(message):
#     print("Urban message")
    
@dp.message_handler(commands=['start']) 
async def start_message(message):
    kb = [
        [
            types.KeyboardButton(text="Рассчитать"),
            types.KeyboardButton(text="Информация")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = keyboard)
    # print("Привет! Я бот помогающий твоему здоровью.")
    
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    # print("Введите команду /start, чтобы начать общение.")
    
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)