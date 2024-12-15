from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import FSInputFile, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio
import os

from dotenv import load_dotenv
from crud_functions import get_all_products, is_included, add_user

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

load_dotenv()

file_names = {'Помидоры': ('tomato.jpg', 1), 'Баклажаны': ('eggplant.jpg', 2), 'Лук': ('onion.jpg', 3), 'Картофель': ('potato.jpg', 4)}

kb_list = [
    [
        KeyboardButton(text="Рассчитать"),
        KeyboardButton(text="Информация"),
        KeyboardButton(text="Купить"), 
        KeyboardButton(text="Регистрация")
    ]
]

start_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_list)

 
inline_kb_list = [
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
]
reply_markup_1 = InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

inline_kb_list_2 = [
    [InlineKeyboardButton(text=f'{list(file_names.keys())[0]}', callback_data=f'product_buying')],
    [InlineKeyboardButton(text=f'{list(file_names.keys())[1]}', callback_data='product_buying')],
    [InlineKeyboardButton(text=f'{list(file_names.keys())[2]}', callback_data='product_buying')],
    [InlineKeyboardButton(text=f'{list(file_names.keys())[3]}', callback_data='product_buying')],

]
# inline_kb = InlineKeyboardBuilder().add(button1, button2) 
reply_markup_2 = InlineKeyboardMarkup(inline_keyboard=inline_kb_list_2)

class UserState(StatesGroup):
    # adress = State()
    age = State()
    growth = State()
    weight = State()
   

class RegistrationState(StatesGroup):
    # adress = State()
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message(F.text == "Регистрация")
async def sing_up(message, state):
# Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
# Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
# После ожидать ввода имени в атрибут RegistrationState.username при помощи метода set.
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)

@dp.message(RegistrationState.username)    
async def set_username(message, state):
    
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await state.set_state(RegistrationState.username)
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await state.set_state(RegistrationState.email)
# Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
# Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text. Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
# Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и запрашивать новое состояние для RegistrationState.username.

@dp.message(RegistrationState.email)    
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)
# Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
# Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
# Далее выводить сообщение "Введите свой возраст:":
# После ожидать ввода возраста в атрибут RegistrationState.age.

@dp.message(RegistrationState.age)    
async def set_age(message, state):
    await state.update_data(age=message.text)
    
    
# Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
# Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
# Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users при помощи ранее написанной crud-функции add_user.
# В конце завершать приём состояний при помощи метода finish().    
    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = int(data['age'])
    add_user(username, email, age)
    await message.answer(f"Спасибо за регистрацию, {username}! Ваши данные сохранены.")
    await state.clear()  
    

@dp.message(F.text == 'Рассчитать')
async def main_menu(message):

    await message.answer("Выберите опцию:", reply_markup = reply_markup_1)

@dp.message(F.text == "Купить")
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        image_from_pc = FSInputFile(f'module14\\Доработка бота\\{product[4]}.jpg')
        await message.answer_photo(image_from_pc)
    await message.answer("Выберите продукт для покупки:", reply_markup=reply_markup_2)
    

@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')

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