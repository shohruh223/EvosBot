from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default.menu import key_button, keybo_button, vakansi2_menu, vakansi3_menu, \
    keybor_button, keybordi_button, gain_menu
from loader import dp


@dp.message_handler(Text(equals="💼 Вакансии"))
async def st(message: types.Message):
    await message.answer("Присоединяйтесь в команду EVOS!")
    await message.answer("📍 Выберите регион:",
                         reply_markup=key_button())


@dp.message_handler(Text(equals="💼 Bo'sh ish o'rinlari"))
async def start(message: types.Message):
    await message.answer("Reioningizni tanlang",
                         reply_markup=gain_menu())


@dp.message_handler(Text(equals="Андижан"))
async def dh(message: types.Message):
    await message.answer("💼 Выберите интересующую Вас вакансию",
                         reply_markup=vakansi2_menu())


@dp.message_handler(Text(equals="Универсальный сотрудник"))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
        caption="""
📌Возраст от 18 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Свободный график(желательно)

✔️Опрятный внешний вид 

💰 Зарплата от 13 500( с учетом вычета НДФЛ) тысяч сум за 1 час""")
    await message.answer("""
❇️ В каком филиале вы хотите работать?""",
                         reply_markup=keybor_button())


@dp.message_handler(Text(equals="Курьер."))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSO136PmflDFiup0SDzZYhTBeBe-J-z3pyvGyHRXHy1HjL1JKIH",
        caption="""📌 Возраст от 20 до 35 

🇷🇺/🇺🇿  Владение русским и узбекским языком

🕑 Свободный график(желательно)

👨‍💼/👩‍💼 Опрятный внешний вид 

🚘Наличие своего транспорта

📍ЗП в зависимости от локации и региона""")
    await message.answer("""
👤 Введите полное ФИО.
(пример: Иван Иванов Иванович)""",
                         reply_markup=keybo_button())


@dp.message_handler(Text(equals="Коканд"))
async def dh(message: types.Message):
    await message.answer("💼 Выберите интересующую Вас вакансию",
                         reply_markup=vakansi3_menu())


@dp.message_handler(Text(equals="Универсальный сотрудник."))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
        caption="""
📌Возраст от 18 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Свободный график(желательно)

✔️Опрятный внешний вид 

💰 Зарплата от 13 500( с учетом вычета НДФЛ) тысяч сум за 1 час""")
    await message.answer("""
❇️ В каком филиале вы хотите работать?""",
                         reply_markup=keybordi_button())
