import asyncio
import json
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

# ТВОИ ДАННЫЕ
TOKEN = "8444462509:AAEHhQRzXP1UG9KekXH-nTtLT5VLO0Vs084"
ADMIN_ID = 6042618441
URL = "https://timfounder.github.io/abiturient/" # Ссылка на твой GitHub Pages

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Создаем кнопку, которая открывает мини-приложение
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Anketani to'ldirish 📝", web_app=WebAppInfo(url=URL))]
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}! 👋\n\n"
        "Chet elda ta'lim olish bo'yicha anketani to'ldirish uchun pastdagi tugmani bosing 👇",
        reply_markup=kb
    )

# Этот блок будет ловить данные, если ты решишь вернуться к безопасной отправке через бот
@dp.message(F.web_app_data)
async def handle_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    # Здесь можно прописать логику ответа после заполнения
    await message.answer("Rahmat! Ma'lumotlaringiz qabul qilindi. ✅")

async def main():
    print("Bot ishga tushdi... 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
