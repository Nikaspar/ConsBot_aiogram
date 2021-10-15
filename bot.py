import logging
from aiogram import Bot, Dispatcher, executor, types
from config import token
from datetime import datetime
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
    await message.answer('Привет!\nЭтот бот поможет с ошибками\nв работе Консультант Плюс.\n'
                         '\nПросто введите номер ошибки\n'
                         'и увидите, что она значит,\n'
                         'и как исправить.')


@dp.message_handler(content_types='text')
async def send_description(message: types.Message):
    """
    This handler will send error description
    """
    description, status = utils.get_description(message.text)
    await message.answer(description)


@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    """
    This handler receives and saves photos to /storage/
    """
    user = message.from_user.username
    date = datetime.now()
    await message.photo[-1].download(destination_file='storage/{} {}.jpg'.format(user, date.strftime('%d-%m-%y %H_%M')))
    await message.answer('Фото сохранено.')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
