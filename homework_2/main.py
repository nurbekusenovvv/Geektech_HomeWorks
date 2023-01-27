from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from pytube import YouTube, exceptions
import config
import logging
import os

bot = Bot(config.token)
print(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
print(dp)
storage = MemoryStorage()
print(storage)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands = ['start', 'go'])
async def start(msg:types.Message):
    kb = [
        [KeyboardButton("/audio")],
        [KeyboardButton("/video")],
        [KeyboardButton("/help")],
        [KeyboardButton("/contact", request_contact=True)],
        [KeyboardButton("/location", request_location=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True,
    input_field_placeholder="Выберите вариант загрузки")
    await msg.answer(f"Здраствуйте {msg.from_user.first_name}", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(msg:types.Message):
    await msg.reply("OK")
    print(msg.contact['phone_number'])

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(msg:types.Message):
    print(msg.location['latitude'])
    print(msg.location['longitude'])
    await bot.send_location(msg.chat.id, msg.location['latitude'], msg.location['longitude'])

@dp.message_handler(commands=['help'])
async def help(msg:types.Message):
    inline_kb = [
        [InlineKeyboardButton("Видео", callback_data = "video")],
        [InlineKeyboardButton("Аудио", callback_data = "audio")]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
    await msg.answer("Вот что я могу", reply_markup=inline_keyboard)

def downloader(url, type):
    yt = YouTube(url)
    if type == "video":
        yt.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download("video", f"{yt.title}.mp4")
        return f"{yt.title}.mp4"
    elif type == "audio":
        yt.streams.filter(only_audio=True).first().download("audio", f"{yt.title}.mp3")
        return f"{yt.title}.mp3"

class DownloadVideo(StatesGroup):
    download = State()

class DownloadAudio(StatesGroup):
    download = State()

@dp.message_handler(commands='video')
async def video(msg:types.Message,callback:types.CallbackQuery):
    await msg.answer(f"Отправьте ссылку и я вам его скачаю")
    await DownloadVideo.download.set()

@dp.callback_query_handlers
@dp.message_handler(commands='audio')
async def audio(msg:types.Message):
    await msg.answer(f"Отправьте ссылку и я вам скачаю его в mp3")
    await DownloadAudio.download.set()

@dp.message_handler(state=DownloadVideo.download)
async def download_video_state(msg:types.Message, state:FSMContext):
    try:
        await msg.answer("Скачиваем видео, ожидайте...")
        title = downloader(msg.text, "video")
        print(title)
        video = open(f'video/{title}', 'rb')
        await msg.answer("Все скачалось, вот видео")
        await bot.send_video(msg.chat.id, video)
    except exceptions.RegexMatchError:
        await msg.answer("Неправильная ссылка")
    except Exception as error:
        await msg.answer(f"Произошла ошибка, повторите еще раз. {error}")
    os.remove(f"video/{title}")
    await state.finish()



@dp.message_handler(state=DownloadAudio.download)
async def download_audio_state(msg:types.Message, state:FSMContext):
    try:
        await msg.answer("Скачиваем аудио, ожидайте...")
        title = downloader(msg.text, "audio")
        audio = open(f'audio/{title}', 'rb')
        await msg.answer("Все скачалось, вот аудио")
        await bot.send_audio(msg.chat.id, audio)
    except exceptions.RegexMatchError:
        await msg.answer("Неправильная ссылка")
    except Exception as error:
        await msg.answer(f"Произошла ошибка, повторите еще раз. {error}")
    os.remove(f"audio/{title}")
    await state.finish()

executor.start_polling(dp)