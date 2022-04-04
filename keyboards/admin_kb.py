from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#knopki klaviaturi abmina
button_load = KeyboardButton('/Yuklash')
button_delete = KeyboardButton('/uchirish')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
    .add(button_delete)