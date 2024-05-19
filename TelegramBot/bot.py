from aiogram import Bot, Dispatcher, executor, types

token = '6748303556:AAG1_974wTSuyYcXKidIlaMZL_uif8Sv7LQ'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.count(' ') >= 1:
     await message.answer(text=message.text.capitalize())

if __name__ == "__main__":
    executor.start_polling(dp)