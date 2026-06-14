import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import os
TOKEN = os.getenv("8635030604:AAFOUJg7nPogKWqUpzjbsbAJAyfNe8mDq6k")

bot = Bot("8635030604:AAFOUJg7nPogKWqUpzjbsbAJAyfNe8mDq6k")
dp = Dispatcher()

# Клавиатура
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог")]
    ],
    resize_keyboard=True
)

# /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Всем привет, я Ренатка 🌸\n\n"
        "Мне 20 лет.\n"
        "Здесь ты можешь посмотреть фотки и купить их 💜\n\n"
        "Нажми «Каталог» 👇",
        reply_markup=kb
    )

# кнопка каталог
@dp.message(F.text == "🛍 Каталог")
async def catalog(message: Message):
    await message.answer("Каталог скоро появится 💜")

# запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
