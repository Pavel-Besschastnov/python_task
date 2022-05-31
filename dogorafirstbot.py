import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5592669524:AAEaXPNF-T_0HjiscIfq8lhCV40WPLBuRNQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
