from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default.menu import filial_menu, filial_menu_ru
from loader import dp, bot


@dp.message_handler(Text("📍 Samarqand Darvoza"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Samarqand Darvoza"
Adres: kocha. Qoratjsh, 5А""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3160488,
                            longitude=69.2297722)


@dp.message_handler(Text(equals="↩️ Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=filial_menu())


@dp.message_handler(Text("📍 Alayskiy bozor"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Alayskiy bozor"
Adres: joy. Amir Temur, 42""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3204956,
                            longitude=69.2802406)


@dp.message_handler(Text("📍 Malika"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Malika"
Adres:  kocha. Bagiravon, 29""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3236641,
                            longitude=69.1652273)


@dp.message_handler(Text("📍 Yahyo Gulamov, 94"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Yahyo Gulamov, 94"
Adres:  kocha Yahyo Gulamov, 94""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3052033,
                            longitude=69.2817854)


@dp.message_handler(Text(equals="📍Samarqand Darvoza"))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://static-pano.maps.yandex.ru/v1/?panoid=1486723667_804149084_23_1571463763&size=500%2C240&azimuth=-148.4&tilt=10&api_key=maps&signature=6qI_xL-iwhZxvBoBOGVQQP_eAoeqTpvLq8UdrzT-ils=",
        caption="""Филиал: "Самарканд дарвоза"

Адрес: ул. Коратош, 5А""")
    await message.answer_location(longitude=41.315650,
                                  latitude=69.231901)


@dp.message_handler(Text(equals="📍Алайский базар"))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPpzuPa8skCx39lq50t_RyU39M6EUr7lqSdhDjwdVJ5X03nxa_",
        caption="""Филиал: Алайский базар

Адрес: просп. Амира Темура, 42

Контакты: +998 71 203 12 12""")
    await message.answer_location(longitude=41.321049,
                                  latitude=69.286896)


@dp.message_handler(Text(equals="📍Малика"))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUS4y1LJ7w92FfZJ_B8qMmwFmlpX0f33vktWgBAVdNNKLs6g_3",
        caption="""Филиал: Малика

Адрес: ул. Богиравон, 29

Контакты: +998 71 203 12 12""")
    await message.answer_location(longitude=41.265161,
                                  latitude=69.175532)


@dp.message_handler(Text(equals="📍Яхъё Гулямова,94"))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS0vWDgdGEtwaXix81OqYiKrS5s-0Nqo8-ARZzLZHwgL8MdUPa3",
        caption="""Филиал: улица Яхъё Гулямова, 94

Адрес: улица Яхъё Гулямова, 94

Контакты: +998 71 203 12 12""")
    await message.answer_location(longitude=41.304775,
                                  latitude=69.284611)


@dp.message_handler(Text(equals="⬅️ Назад"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=filial_menu_ru())
