from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.default.menu import language_uz, main_menu_ru
from loader import dp


@dp.message_handler(Text(equals="🇺🇿/🇷🇺 Til"))
async def language(message: types.Message):
    await message.answer(text="Tilni o'zgartirish",
                         reply_markup=language_uz())


@dp.message_handler(Text(equals="🇷🇺 Русский"))
async def language_ru(message: types.Message):
    await message.answer(text="Выбрано: 🇷🇺 Русский")
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu_ru())
