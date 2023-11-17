from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 Kompaniya haqida"), KeyboardButton(text="📍 Fililallar"))
    rkm.row(KeyboardButton(text="💼 Bo'sh ish o'rinlari"))
    rkm.row(KeyboardButton(text="Menyu"), KeyboardButton(text="🗣 Yangiliklar"))
    rkm.row(KeyboardButton(text="📞 Kontaktlar/Manzil"), KeyboardButton(text="🇺🇿/🇷🇺 Til"))
    return rkm


def main_menu_ru():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 О компании"), KeyboardButton(text="📍 Филиалы"))
    rkm.row(KeyboardButton(text="💼 Вакансии"))
    rkm.row(KeyboardButton(text="📱 Меню"), KeyboardButton(text="🗣 Новости"))
    rkm.row(KeyboardButton(text="📞 Контакты/Адрес"), KeyboardButton(text="🇺🇿/🇷🇺 Язык"))
    return rkm


def filial_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Yaqin filiallarni ko'rsatish"))
    rkm.row(KeyboardButton(text="🏢 Bosh ofis"), KeyboardButton(text="Toshkent sh."))
    rkm.row(KeyboardButton(text="⬅️ Ortga"))
    return rkm


def filial_menu_ru():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Показать ближайший филиал"))
    rkm.row(KeyboardButton(text="🏢 Главный Офис"), KeyboardButton(text="г. Ташкент"))
    rkm.row(KeyboardButton(text="⬅️ Назад"))
    return rkm


def nain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Locatsiya jonatish"))
    rkm.row(KeyboardButton(text="🔙 Ortga"))
    return rkm


def kain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Samarqand Darvoza"), KeyboardButton(text="📍 Alayskiy bozor"))
    rkm.row(KeyboardButton(text="📍 Malika"), KeyboardButton(text="📍 Yahyo Gulamov, 94"))
    rkm.row(KeyboardButton(text="↩️ Ortga"))
    return rkm


def fmain_menu2():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍Samarqand Darvoza"), KeyboardButton(text="📍Алайский базар"))
    rkm.row(KeyboardButton(text="📍Малика"), KeyboardButton(text="📍Яхъё Гулямова,94"))
    rkm.row(KeyboardButton(text="⬅️ Назад"))
    return rkm


def gain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Toshkent"), KeyboardButton(text="Andijoon"))
    rkm.row(KeyboardButton(text="Kokond"), KeyboardButton(text="Namangan"))
    rkm.row(KeyboardButton(text="Toshkent viloyati"), KeyboardButton(text="Samarqand"))
    rkm.row(KeyboardButton(text="Fargona"), KeyboardButton(text="Xorezm viloyati"))
    rkm.row(KeyboardButton(text="Navoi"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="◀️ Ortga"))
    return rkm


def fain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal hodim"), KeyboardButton(text="Operator"))
    rkm.row(KeyboardButton(text="Etkazib beruvchi"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="⏪ Ortga"))
    return rkm


#
# def key_button():
#     rk = ReplyKeyboardMarkup(resize_keyboard=True)
#     rk.row(KeyboardButton(text="Тошкент"), KeyboardButton(text="Андижан"))
#     rk.row(KeyboardButton(text="Коканд"), KeyboardButton(text="Наманган"))
#     rk.row(KeyboardButton(text="Ташкентская область"), KeyboardButton(text="Самарканд"), )
#     rk.row(KeyboardButton(text="Фергана"), KeyboardButton(text="Хорезмская область"))
#     rk.row(KeyboardButton(text="Наваи"))
#     rk.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
#     return rk


def qain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal hodim"), KeyboardButton(text="Operator"))
    rkm.row(KeyboardButton(text="Etkazib beruvchi"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="⏮ Ortga"))
    return rkm


def pain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Chilonzor rayon"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="🔚 Ortga"))
    return rkm


def lain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="Ortga"))
    button = KeyboardButton(text="Register")
    rkm.add(button)
    return rkm


def cancel():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="cancel")
    rkm.add(button)
    return rkm


def wain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Chilonzor rayon"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="🔚 Ortga"))
    return rkm


def cain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="Ortga"))
    button = KeyboardButton(text="Register")
    rkm.add(button)
    return rkm


def language_uz():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha"))
    rkm.row(KeyboardButton(text="⬅️ Ortga"))
    return rkm


def language_ru():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha"))
    rkm.row(KeyboardButton(text="🔙 Назад"))
    return rkm


def key_button():
    rk = ReplyKeyboardMarkup(resize_keyboard=True)
    rk.row(KeyboardButton(text="Тошкент"), KeyboardButton(text="Андижан"))
    rk.row(KeyboardButton(text="Коканд"), KeyboardButton(text="Наманган"))
    rk.row(KeyboardButton(text="Ташкентская область"), KeyboardButton(text="Самарканд"), )
    rk.row(KeyboardButton(text="Фергана"), KeyboardButton(text="Хорезмская область"))
    rk.row(KeyboardButton(text="Наваи"))
    rk.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rk


def gain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Toshkent"), KeyboardButton(text="Andijoon"))
    rkm.row(KeyboardButton(text="Kokond"), KeyboardButton(text="Namangan"))
    rkm.row(KeyboardButton(text="Toshkent viloyati"), KeyboardButton(text="Samarqand"))
    rkm.row(KeyboardButton(text="Fargona"), KeyboardButton(text="Xorezm viloyati"))
    rkm.row(KeyboardButton(text="Navoi"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="◀️ Ortga"))
    return rkm

def vakansii_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"), KeyboardButton(text="Оператор call-центра"))
    rkm.row(KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def keyb_button():
    rk = ReplyKeyboardMarkup(resize_keyboard=True)
    rk.row(KeyboardButton(text="Юнусабадский р-н"), KeyboardButton(text="Мирзо Улугбекский р-н"))
    rk.row(KeyboardButton(text="Яшнабадский р-н"), KeyboardButton(text="Яккасарайский р-н"))
    rk.row(KeyboardButton(text="Сергилийский р-н"), KeyboardButton(text="Чиланзарский р-н"), )
    rk.row(KeyboardButton(text="Мирабадский р-н"), KeyboardButton(text="Шайхонтохурский р-н"))
    rk.row(KeyboardButton(text="Алмазарский р-н"), KeyboardButton(text="Бектемирский р-н"))
    rk.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rk


def keybo_button():
    rk = ReplyKeyboardMarkup(resize_keyboard=True)
    rk.row(KeyboardButton(text="Чиланзарский р-н"), )
    rk.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rk



def vakansi2_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"), KeyboardButton(text="Курьер."))
    rkm.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def vakansi3_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"))
    rkm.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def keybor_button():
    rkk = ReplyKeyboardMarkup(resize_keyboard=True)
    rkk.row(KeyboardButton(text="Микрорайон 3"),KeyboardButton(text="ТЦ Узбегим"), KeyboardButton(text="Навруз Молл"),)
    rkk.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rkk


def keybordi_button():
    rkk = ReplyKeyboardMarkup(resize_keyboard=True)
    rkk.row(KeyboardButton(text="Коканд"))
    rkk.row(KeyboardButton(text="❌Отмена❌"), KeyboardButton(text="⬅️ Назад"))
    return rkk
