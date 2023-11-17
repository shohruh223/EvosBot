from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.default.menu import vakansii_menu, keyb_button, keybo_button
from loader import dp


@dp.message_handler(Text(equals="Тошкент"))
async def dh(message: types.Message):
    await message.answer("💼 Выберите интересующую Вас вакансию",
                         reply_markup=vakansii_menu())


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
Выберите район где данный момент открыты вакансии.""",
                         reply_markup=keyb_button())


@dp.message_handler(Text(equals="Оператор call-центра"))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWsZLWsqFJrYuB1EiVLQx-akxNenLJJNEiUJhtmNE50ANoyHlZ",
        caption="""📌 Возраст от 18 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Полная занятость

👨‍💼/👩‍💼 Опрятный внешний вид

🧑‍💻/👩‍💻 Наличие ноутбука/компьютера

Мы предоставляем:
-Официальное трудоустройство
-Питание за счет компании
-Предоставление обучения(оплачиваемая)
-Почасовая оплата труда

Период стажировки 2 недели""")
    await message.answer("""
Выберите район где данный момент открыты вакансии.""",
                         reply_markup=keybo_button())


@dp.message_handler(Text(equals="Курьер"))
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
Выберите район где данный момент открыты вакансии.""",
                         reply_markup=keybo_button())