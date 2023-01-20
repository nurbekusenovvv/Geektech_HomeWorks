from aiogram import Bot,Dispatcher,types,executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import config

bot = Bot(token=config.token)
dp = Dispatcher(bot)

backend_button = KeyboardButton("/backend")
frontend_button = KeyboardButton("/frontend")
android_button = KeyboardButton("/android")
ios_button = KeyboardButton("/ios")
uiux_button = KeyboardButton("/UXUI")

buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons.add(backend_button,frontend_button,android_button,ios_button,uiux_button)
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
    await message.answer(f"Длительность 5 мес")

@dp.message_handler(commands=('frontend'))
async def front(message: types.Message):
    await message.answer(f"Информация  Frontend")
    await message.answer(f"Стоимость: 10000с")
    await message.answer(f"Длительность 5 мес")

@dp.message_handler(commands=('ios'))
async def ios(message: types.Message):
    await message.answer(f"Информация  IOS")
    await message.answer(f"Стоимость: 10000с")
    await message.answer(f"Длительность 5 мес")

@dp.message_handler(commands=('android'))
async def android(message: types.Message):
    await message.answer(f"Информация  Android")
    await message.answer(f"Стоимость: 10000с")
    await message.answer(f"Длительность 7 мес")


@dp.message_handler(commands=('UXUI'))
async def uxui(message: types.Message):
    await message.answer(f"Информация  UX-UI")
    await message.answer(f"Стоимость: 10000с")
    await message.answer(f"Длительность 3 мес")

executor.start_polling(dp)