import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command(commands="start"))
async def info(message: types.Message):
    button_list = [
        [types.KeyboardButton(text='Open web page', web_app=WebAppInfo(url='https://github.com/vktadm'))],
    ]
    # Inline кнопки в чате
    markup = types.ReplyKeyboardMarkup(keyboard=button_list, one_time_keyboard=True)
    await message.reply('Hello 🦁', reply_markup=markup)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())