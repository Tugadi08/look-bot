import logging

from aiogram import Bot, Dispatcher, executor, types
from button import *

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(text = "Ortga")
async def echo(message: types.Message):
    await message.answer("Bosh menyu", reply_markup=bosh_menu)


@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nMen Lookbot man\nMenu:\nBurger\nLavash\nHot-dog\nPizza\nGamburger\nChizburger\nDoubleburger\nTvister\nSalat", reply_markup=bosh_menu)


@dp.message_handler(text = "Ichimliklar")
async def echo(message: types.Message):
    await message.answer("Ichimliklar bo'limi", reply_markup=ichimliklar_menu)


@dp.message_handler(text = "Lavash")
async def echo(message: types.Message):
    await message.answer("25.000 so'm")


@dp.message_handler(text = "Burger")
async def echo(message: types.Message):
    await message.answer("15.000 so'm")


@dp.message_handler(text = "Hot-dog")
async def echo(message: types.Message):
    await message.answer("17.000 so'm")

@dp.message_handler(text = "Pizza")
async def echo(message: types.Message):
    await message.answer("95.000 so'm")


@dp.message_handler(text = "Gamburger")
async def echo(message: types.Message):
    await message.answer("23.000 so'm")


@dp.message_handler(text = "Chizburger")
async def echo(message: types.Message):
    await message.answer("26.000 so'm")


@dp.message_handler(text = "Doubleburger")
async def echo(message: types.Message):
    await message.answer("15.000 so'm")


@dp.message_handler(text = "Tvister")
async def echo(message: types.Message):
    await message.answer("35.000 so'm")


@dp.message_handler(text = "Salat")
async def echo(message: types.Message):
    await message.answer("10.000 so'm")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Unaqasi bizda yo'q")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

