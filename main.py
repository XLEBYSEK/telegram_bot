import asyncio
from email import message
import random
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from media import media


bot = Bot(token="7592600913:AAFtL4qAI5_b1iQlyC_ASgXKVUmCyqGc90U")
dp = Dispatcher()
router = Router()
dp.include_router(router)


def get_random_img():
    try:
        urls = media.get('images', [])
        print(urls)
        return random.choice(urls) if urls else None
    except Exception:
        return None

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [

        [types.KeyboardButton(text="/КНБ Камень")],
        [types.KeyboardButton(text="/КНБ Ножницы")],
        [types.KeyboardButton(text="/КНБ Бумага")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выбери камень, ножницы или бумагу", reply_markup=keyboard)

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


@dp.message(Command('КНБ'))
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


