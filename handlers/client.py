from aiogram import types
from aiogram import Dispatcher
from creare_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#chat_id = '775451970'
import sys
import locale
#reload(sys)
# sys.setdefaulttencoding


#urlkb = InlineKeyboardMarkup(row_width=1)
#urlButton = InlineKeyboardButton(text='admin 1', url = 'https://t.me/komiltuev')
#urlButton2 = InlineKeyboardButton(text='admin 2', url = 'https://t.me/komiltuev00')
#urlkb.add(urlButton, urlButton2)

tiluzb = InlineKeyboardMarkup(row_width=1)
tiluzbButton = InlineKeyboardButton(text='uzb', callback_data='uzb')
tiluzb.add(tiluzbButton)

tileng = InlineKeyboardMarkup(row_width=1)
tilengButton = InlineKeyboardButton(text='eng', callback_data='eng')
tileng.add(tilengButton)
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Xush kelibsiz\nKerakli tilni tanlang\nChoose your language!', reply_markup=kb_client)
        #await message.answer('adminlar: ', reply_markup=urlkb)
        await message.answer('uzbek tili: ', reply_markup=tiluzb)
        #await message.answer('english: ', reply_markup=tileng)
    except:
        await message.reply('admin bilan boglanish uchun:@komil1bot')


@dp.callback_query_handler(text='uzb')
async def tiluzb_call(callback : types.CallbackQuery):
    await callback.answer('til tanlandi (bizni botda hozircha uzbek tili mavjud)')


#@dp.callback_query_handler(text='eng')
#async def tileng_call(callback : types.CallbackQuery):
 #   await callback.answer('choosed language')


#@bot.message_handler(func=lambda message : True)
#def echo_message(message):
#    bot.send_message(chat_id = chat_id, text=message.text)

#@dp.message_handler(commands=['Ish_vaqti'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'tunu kun xizmatizdamiz kuniga 24 soat')

#@dp.message_handler(commands=['Adress'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Narpay kucha 77/44dom\nOrentir Family Park')

async def pizza_nomer_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Adminstrator: @komiltuev')

pissa = InlineKeyboardMarkup(row_width=1)
pissaButton = InlineKeyboardButton(text='tanlash', callback_data='qqqq')
pissa.add(pissaButton)
#@dp.message_handler(commands=['Menyu'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)
    await message.answer('pitsani tanlang', reply_markup=pissa)
@dp.callback_query_handler(text='qqqq')
async def qqqq_call(callback : types.CallbackQuery):
    await callback.answer('pizza tanlandi\nBuyurtmangiz 15 daqiqada yetkazib beriladi')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start,commands=['start', 'help'])
#    dp.register_message_handler(echo_message, func=lambda message: True)
    dp.register_message_handler(pizza_open_command,commands=['Ishlash_Vaqtimiz'])
    dp.register_message_handler(pizza_place_command,commands=['Adresimiz'])
    dp.register_message_handler(pizza_menu_command, commands=['Menyu'])
    dp.register_message_handler(pizza_nomer_command, commands=['Adminstrator'])

