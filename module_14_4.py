from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *
import asyncio
import aiogram

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.add(button, button2)
kb.add(button3)
kb_line = InlineKeyboardMarkup()
button_line = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button_line2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
kb_line.add(button_line)
kb_line.add(button_line2)
kb_line_2 = InlineKeyboardMarkup()
black = InlineKeyboardButton (text = 'Черный врум', callback_data='product_buying')
blue = InlineKeyboardButton (text = 'Голубой врум', callback_data='product_buying')
orange = InlineKeyboardButton (text = 'Оранжевый врум', callback_data='product_buying')
yelow = InlineKeyboardButton (text = 'Желтый врум', callback_data='product_buying')
kb_line_2.add(black, blue, orange, yelow)
prod_start = get_all_products

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb_line)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer ()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    if products:
        for product in products:
            await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]} ")
            with open(f'product/{product[0]}.png', "rb") as img:
                await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_line_2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer ()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост в сантиметрах:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {bmr} ккал в день.')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start_commands(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью. Я могу рассчитать вашу норму калорий.",
                         reply_markup=kb)

@dp.message_handler(text = 'Информация')
async def information(message):
    await message.answer('Кнопка еще не готова')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
