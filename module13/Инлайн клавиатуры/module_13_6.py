from aiogram import Bot, Dispatcher, types 
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio
import os

from dotenv import load_dotenv

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

load_dotenv()



kb_list = [
    [
        KeyboardButton(text="Рассчитать"),
        KeyboardButton(text="Информация")
    ]
]

start_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_list)

 
inline_kb_list = [
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
]
builder = InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
# inline_kb = InlineKeyboardBuilder().add(button1, button2) 


class UserState(StatesGroup):
    # adress = State()
    age = State()
    growth = State()
    weight = State()
    
@dp.message(F.text == 'Рассчитать')
async def main_menu(message):

    await message.answer("Выберите опцию:", reply_markup = builder)

# @dp.callback_query(lambda callback_query: True)
# async def handle_callback_query(callback_query: CallbackQuery):
#     # Обработка нажатия на кнопку
#     print ('Вы нажали на кнопку!')
#     await callback_query.message.answer('Вы нажали на кнопку!')

#     await callback_query.answer('Вы нажали на кнопку!')

@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    formula = ("Для мужчин: 10 × вес (кг) + 6.25 × рост (см) - 5 × возраст (лет) + 5")
    await call.message.answer(formula)
    await call.answer()

@dp.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery,  state):
    await call.message.answer("Введите ваш возраст:")
    await call.answer()
    await state.set_state(UserState.age)
    
@dp.message(UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await state.set_state(UserState.growth)
    
@dp.message(UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
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
    await state.clear()    
    
# @dp.message_handler(text = ['Urban', 'ff']) 
# async def urban_message(message):
#     print("Urban message")
    
@dp.message(Command('start')) 
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = start_menu)
    # print("Привет! Я бот помогающий твоему здоровью.")
    
@dp.message(F.text == 'Информация')
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    # print("Введите команду /start, чтобы начать общение.")
    
    
async def main():


    await dp.start_polling(bot)    
    
if __name__ == "__main__":
    asyncio.run(main())