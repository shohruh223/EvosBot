from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals="🏢 Kompaniya haqida"))
async def about_company(message: types.Message):
    await message.answer_photo(photo="https://jolbors.com/media/works/991/615214f7210e6.jpg",
                               caption="""EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!""")


@dp.message_handler(Text(equals="🏢 О компании"))
async def about_company_ru(message: types.Message):
    await message.answer_photo(photo="https://jolbors.com/media/works/991/615214f7210e6.jpg",
                               caption="""Информация о компании:

Сеть ресторанов быстрого обслуживания EVOS® не стоит на месте, а постоянно растет и развивается вместе с вами и для вас! Мы расширяем свою географию и открываем новые филиалы практически каждый месяц. 
Сейчас в нашей сети насчитывается более 50 филиалов по всему Узбекистану. Поэтому мы всегда в поиске динамичных и активных людей, которые хотят стать частью нашей команды и готовы строить свою карьеру в EVOS®. 
EVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и перспективы карьерного роста. 
Начни свою карьеру в EVOS® уже сейчас!""")
