import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv "8635030604:AAFOUJg7nPogKWqUpzjbsbAJAyfNe8mDq6k"

bot = Bot(token=TOKEN)
dp = Dispatcher()

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🛍 Каталог")]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет 👋", reply_markup=kb)

@dp.message(F.text == "🛍 Каталог")
async def catalog(message: Message):
    await message.answer("Каталог скоро будет")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
