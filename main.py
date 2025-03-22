import asyncio
from email import message
import random
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from media import media

bot = Bot(token="7592600913:AAFtL4qAI5_b1iQlyC_ASgXKVUmCyqGc90U")
dp = Dispatcher()

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_knb)
button_knb = KeyboardButton('КНБ')

def get_random_img():
    try:
        urls = media.get('images', [])
        print(urls)
        return random.choice(urls) if urls else None
    except Exception:
        return None

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.greet_kb)


@dp.message(Command('img'))
async def cmd_img(message: types.message):
    try:
        url = get_random_img()
        print(url)
        if url:
            await message.answer_photo(url)
        else:
            await message.text('пошел ты')
    except Exception as e:
        await message.answer(str(e))


@dp.message(Command('echo'))
async def cmd_echo(message: types.message):
    print('/echo')
    text = message.text.replace('/echo', '').strip()
    if text:
        await message.answer(text)
    else:
        await message.answer('и че это щас было')


@dp.message_handler(Command['КНБ'])
async def game(message: types.Message):
    knb = ['камень', 'ножницы', 'бумагу']
    bot = random.choice(knb)
    user = message.text.replace('/КНБ', '').strip()
    if bot == user:
        result = bot
        await message.answer('Ничья')
    elif (bot == 'камень' and user == 'ножницы') or (bot == 'ножницы' and user == 'бумагу') or (bot == 'бумагу' and user == 'камень'):
        result = bot
        await message.answer(f'Ты проиграл! бот выбрал {result}')
    else:
        result = bot
        await message.answer(f'Ты выйграл! бот выбрал {result}')
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


