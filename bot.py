import logging
from aiogram import Bot, Dispatcher, executor, types
from config import token
import utils


API_TOKEN = token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will save user's data in db
    and send start message
    """
    utils.save_user(message.get_current())
    await message.answer('Привет!\nЭтот бот поможет с ошибками\nв работе Консультант Плюс.\n'
                         '\nПросто введите номер ошибки\n'
                         'и увидите, что она значит,\n'
                         'и как исправить.')


@dp.message_handler(content_types='text')
async def send_description(message: types.Message):
    """
    This handler will send error description
    """
    description = utils.get_description(message.text)
    await message.answer(description)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
