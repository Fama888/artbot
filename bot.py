import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
import threading

TOKEN = os.getenv"8635030604:AAFOUJg7nPogKWqUpzjbsbAJAyfNe8mDq6k"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===== TELEGRAM =====

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет 👋", reply_markup=kb)

@dp.message(F.text == "🛍 Каталог")
async def catalog(message: Message):
    await message.answer("Открываю каталог...")

async def telegram_bot():
    await dp.start_polling(bot)

# ===== WEB APP =====

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🛍 Каталог работает</h1>
    <p>Теперь это твой Web App</p>
    """

def run_web():
    app.run(host="0.0.0.0", port=10000)

# ===== RUN BOTH =====

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    asyncio.run(telegram_bot())
