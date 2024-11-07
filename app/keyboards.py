from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

default = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

resume = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Anketa to'ldirish 📝")],
], resize_keyboard=True)

default_with_skip = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="▶️ O‘tkazib yuborish")],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

gender = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

education = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Oliy"), KeyboardButton(text='Magistratura')],
    [KeyboardButton(text="Talaba"), KeyboardButton(text="O'rta maxsus")],
    [KeyboardButton(text="O'rta")],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

family_status = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Turmush qurgan"), KeyboardButton(text='Turmush qurmagan')],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

region = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Qoraqalpog‘iston Respublikasi"), KeyboardButton(text='Andijon viloyati')],
    [KeyboardButton(text="Buxoro viloyati"), KeyboardButton(text='Jizzax viloyati')],
    [KeyboardButton(text="Qashqadaryo viloyati"), KeyboardButton(text='Navoiy viloyati')],
    [KeyboardButton(text="Namangan viloyati"), KeyboardButton(text='Samarqand viloyati')],
    [KeyboardButton(text="Surxandaryo viloyati"), KeyboardButton(text='Sirdaryo viloyati')],
    [KeyboardButton(text="Toshkent viloyati"), KeyboardButton(text='Farg\'ona viloyati')],
    [KeyboardButton(text="Xorazm viloyati"), KeyboardButton(text='Toshkent Shahri')],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

branch = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

post = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

from_vacancy_info = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

experience = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Tajribam yo'q"), KeyboardButton(text='1 yildan 3 yilgacha')],
    [KeyboardButton(text="3 yildan 6 yilgacha"), KeyboardButton(text='6 yildan yuqori')],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

yes_or_no = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Ha"), KeyboardButton(text='Yo\'q')],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

phone = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📞 Telegram akkaunt raqamini yuborish", request_contact=True)],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

shirt_size = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="XS / 44 / 37"), KeyboardButton(text='S / 46 / 38')],
    [KeyboardButton(text="M / 48 / 39"), KeyboardButton(text='L / 50 / 40')],
    [KeyboardButton(text="XL / 52 / 41"), KeyboardButton(text='XXL / 54 / 41-42')],
    [KeyboardButton(text="XXXL / 56 / 43-44"), KeyboardButton(text='4XL / 58 / 45-46')],
    [KeyboardButton(text='5XL / 60 / 47-48')],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

is_familiar_works_here = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Yo\'q')],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

education_type = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kunduzgi"), KeyboardButton(text='Sirtqi')],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

finish = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Men roziman")],
    [KeyboardButton(text="Orqaga ↩️"), KeyboardButton(text='Bekor qilish 🚫')],
], resize_keyboard=True)

