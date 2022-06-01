import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5592669524:AAEaXPNF-T_0HjiscIfq8lhCV40WPLBuRNQ'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Калькулятор с рац. числами',
               'калькулятор с комплексными числами']
    keyboard.add(*buttons)
    await message.answer('Выберите режим работы :', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Калькулятор с рац. числами', reply_marcup=KeyboardInterrupt)
async def racion(message: types.message):
    # @bot.messsage_handler(content_types=['text'])

    await message.answer('text')


# def summ():
 #   text1 = eval('text')
#    return text1


@dp.message_handler(lambda message: message.text == 'калькулятор с комплексными числами')
async def racion(message: types.message):

    await message.answer('werwer')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
