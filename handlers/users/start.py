from aiogram import types
from keyboards.default.menu import main_menu
from loader import dp


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())
