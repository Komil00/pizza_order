from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Ishlash_Vaqtimiz')
b2 = KeyboardButton('/Adresimiz')
b3 = KeyboardButton('/Menyu')
b4 = KeyboardButton('Nomeringizni_Yuboring', request_contact=True)
b5 = KeyboardButton('Adresingizni_Yuboring', request_location=True)
b8 = KeyboardButton('/Adminstrator')
#b6 = KeyboardButton('/Yuklash')
#b7 = KeyboardButton('zakaz_otmen')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2,b3).row(b4,b5,b8)#.row(b6,b7)
#kb_client.row(b1,b2,b3)