
import aiogram
import asyncio
import random 
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(token='8730550650:AAG23hZTzYE5hrgNPsJoI9rhWwcmFBWP41Q')
dp = Dispatcher()

@dp.message(Command("start"))
async def on_message(message: types.Message):
    await message.answer('Привет! Я бот, который поможет тебе с выбором случайного числа. Введи команду /random, чтобы получить случайное число от 1 до 100.')
@dp.message(Command("random"))
async def on_random(message: types.Message):
    random_number = random.randint(1, 100)
    await message.answer(f'Твое случайное число: {random_number}')
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
