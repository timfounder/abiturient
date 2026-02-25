import asyncio
import json
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

# НАСТРОЙКИ
TOKEN = "8444462509:AAEHhQRzXP1UG9KekXH-nTtLT5VLO0Vs084"
ADMIN_ID = 6042618441
URL = "https://timfounder.github.io/abiturient/" 

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1. Ответ на команду /start
@dp.message(CommandStart())
async def start(message: types.Message):
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

# 2. Получение данных из HTML и отправка тебе (админу)
@dp.message(F.web_app_data)
async def handle_data(message: types.Message):
    # Распаковываем данные
    d = json.loads(message.web_app_data.data)
    
    # Собираем красивое сообщение
    msg = (
        f"<b>🚀 YANGI ARIZA!</b>\n\n"
        f"👤 <b>Ism:</b> {d['name']}\n"
        f"📅 <b>Sana:</b> {d['dob']}\n"
        f"📞 <b>Tel:</b> {d['phone']}\n"
        f"🏫 <b>Holati:</b> {d['study']}\n"
        f"📜 <b>Sertifikat:</b> {d['cert']} ({d['score']})\n"
        f"💼 <b>Soha:</b> {d['field']}\n"
        f"🌍 <b>Davlat:</b> {d['country']}\n"
        f"🎓 <b>Daraja:</b> {d['level']}"
    )

    # Отправляем сообщение тебе
    await bot.send_message(ADMIN_ID, msg, parse_mode="HTML")
    
    # Отправляем сообщение студенту
    await message.answer(
        "Rahmat! Ma'lumotlaringiz muvaffaqiyatli qabul qilindi. ✅\n"
        "Tez orada mutaxassislarimiz siz bilan bog'lanishadi."
    )

async def main():
    print("Bot ishga tushdi... 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
