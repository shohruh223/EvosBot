from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(equals="Menyu"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://static.tildacdn.com/tild6333-3963-4534-b062-636331353739/14.png",
                               caption="<a href='https://evos.uz/'>Evos saytiga o'tish</a>",
                               parse_mode="HTML")
    await message.answer(text="<a href='https://www.instagram.com/evosuzbekistan/'>Instagram</a>|<a href='https://t.me/evosdeliverybot'>Telegram</a>|<a href='https://www.facebook.com/evosuzbekistan/'>Facebook</a>",
                         parse_mode="HTML")


@dp.message_handler(Text(equals="📱 Меню"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://static.tildacdn.com/tild6333-3963-4534-b062-636331353739/14.png",
                               caption="<a href='https://evos.uz/'>Перейти на сайт Evos</a>",
                               parse_mode="HTML")
    await message.answer(
        text="<a href='https://www.instagram.com/evosuzbekistan/'>Instagram</a>|<a href='https://t.me/evosdeliverybot'>Telegram</a>|<a href='https://www.facebook.com/evosuzbekistan/'>Facebook</a>",
        parse_mode="HTML")
