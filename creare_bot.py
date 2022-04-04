from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

storage=MemoryStorage()

API_TOKEN = '2142956675:AAE488Onont0uce78v5Wj8nmwMVKMrmJ_6A'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)