from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.default.menu import filial_menu, main_menu, nain_menu, kain_menu, filial_menu_ru, main_menu_ru, \
    fmain_menu2
from loader import dp, bot


@dp.message_handler(Text(equals="📍 Fililallar"))
async def start(message: types.Message):
    await message.answer_photo(photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
                               reply_markup=filial_menu(),
                               caption="""EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.

Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!""")


@dp.message_handler(Text(equals="📍 Филиалы"))
async def start(message: types.Message):
    await message.answer_photo(photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
                               reply_markup=filial_menu_ru(),
                               caption="""EVOS - крупнейшая фастфуд-компания в Узбекистане. На данный момент открыто 49 торговых точек и современное многопрофильное производство.""")


@dp.message_handler(Text(equals="⬅️ Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())


@dp.message_handler(Text(equals="⬅️ Назад"))
async def back_ru(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu_ru())


@dp.message_handler(Text(equals="🔙 Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=filial_menu())


@dp.message_handler(Text(equals="☕️ Yaqin filiallarni ko'rsatish"))
async def start(message: types.Message):
    await message.answer_photo(photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
                               reply_markup=nain_menu())


@dp.message_handler(Text("🏢 Bosh ofis"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""📍Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.
📌Ориентир: MAKRO THE TOWER""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3022159,
                            longitude=69.2486216)


@dp.message_handler(Text(equals="🏢 Главный Офис"))
async def st(message: types.Message):
    await message.answer_photo(
        photo="https://static-pano.maps.yandex.ru/v1/?panoid=1486824878_804265745_23_1572248376&size=500%2C240&azimuth=76.8&tilt=10&api_key=maps&signature=CaO7wYSx-bbtQgHXq_MiJRk-RnQb6sn7Ch4cIebYeBw=",
        caption="""Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.
Ориентир: MAKRO THE TOWER""")
    await message.answer_location(longitude=41.30477712672822,
                                  latitude=69.24846406729137)


@dp.message_handler(Text(equals="Toshkent sh."))
async def start(message: types.Message):
    await message.answer_photo(photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
                               reply_markup=kain_menu())


@dp.message_handler(Text(equals="г. Ташкент"))
async def dh(message: types.Message):
    await message.answer("г. Ташкент",
                         reply_markup=fmain_menu2())
