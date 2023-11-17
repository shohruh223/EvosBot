from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp, bot


@dp.message_handler(Text("📞 Kontaktlar/Manzil"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.
📌Ориентир: MAKRO THE TOWER""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=69.275948,
                            longitude=41.287978)


@dp.message_handler(Text(equals="📞 Контакты/Адрес"))
async def st(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               caption="""📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.
                    📌Ориентир: MAKRO THE TOWER
                    📲 Контакты: +998 71 203 12 12""")
    await message.answer_location(longitude=41.30477712672822,
                                  latitude=69.24846406729137)
