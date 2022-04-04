from aiogram import executor
from creare_bot import dp
from data_base import sqlite_db
from handlers import client, admin, other


async def on_startup(_):
    print('Bot onlaynga chiqdi')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

