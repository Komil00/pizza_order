from aiogram import types
from aiogram import Dispatcher
import json,string
from creare_bot import dp

#@dp.message_handler()
async def echo_send(message: types.Message):
   if {i.lower().translate(str.maketrans('', '',string.punctuation)) for i in message.text.split(' ')}\
       .intersection(set(json.load(open('cenz.json')))) != set():
       await message.reply('sukinish mumkun emas')
       await message.delete()
   else:
       await message.reply('siz mavjud bulmagan buruqni yubordingiz\nPastdagi menyulardan')

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)


