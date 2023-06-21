from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6131064408:AAFMdm6OirXjxh_9rt7jr9TLy6k7GIs554Q'

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)


@dp.message_handler()
async def echo_capitalize(message: types.Message):
    await message.answer(text=message.text.upper())
    

if __name__ == "__main__":
    executor.start_polling(dp)