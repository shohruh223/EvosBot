from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(equals="🗣 Yangiliklar"))
async def tell(message: types.Message):
    await message.answer("""Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""")


@dp.message_handler(Text(equals="🗣 Новости"))
async def st(message: types.Message):
    await message.answer(
        """Kompaniya yangiliklari
           Aksiya
           Yangi filiallar
           Yangi tortlar va hk.""")
