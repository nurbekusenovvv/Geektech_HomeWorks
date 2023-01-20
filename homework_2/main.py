from aiogram import Bot,Dispatcher,types,executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import config

bot = Bot(token=config.token)
dp = Dispatcher(bot)

backend_button = KeyboardButton("/backend")

buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons.add(backend_button)
@dp.message_handler(commands=("start"))
async  def start(message : types.Message):
    await message.answer(f'здраствуйте {message.from_user.full_name} Добро пожаловать в гиктек если хотите по больше узнать о гиктек нажмите /help',reply_markup=buttons)

@dp.message_handler(commands=('help'))
async def help(message: types.Message):
    await message.answer(f"Hello")

@dp.message_handler(commands=('backend'))
async def help(message: types.Message):
    await message.answer(f"Информация  Backend")
    await message.answer(f"Стоимость: 10000с")
    await message.answer(f"Стоимость: 10000с")




executor.start_polling(dp)