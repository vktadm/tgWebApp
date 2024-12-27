import asyncio
import json

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command(commands="start"))
async def info(message: types.Message):
    button_list = [
        [types.KeyboardButton(text='Open web page', web_app=WebAppInfo(url='https://vktadm.github.io/tgWebApp/'))],
    ]
    # Inline кнопки в чате
    markup = types.ReplyKeyboardMarkup(keyboard=button_list)
    await message.reply('Hello 🦁', reply_markup=markup)
async def main():
    await dp.start_polling(bot)

@dp.message(F.content_type == types.ContentType.WEB_APP_DATA)
async def get_data(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'The order has been placed ✅\nName: {res["name"]}.'
                         f'\ne-mail: {res["email"]}.\nphone: {res["phone"]}')

if __name__ == "__main__":
    asyncio.run(main())