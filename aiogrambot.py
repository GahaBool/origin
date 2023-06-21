from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6131064408:AAFMdm6OirXjxh_9rt7jr9TLy6k7GIs554Q'

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text)
    else:
        await message.answer(text='Ошибка!')

if __name__ == "__main__":
    executor.start_polling(dp)
    
#hello!