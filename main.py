import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from media import media

bot = Bot(token = "7810431596:AAFSEGLUDo1_ZixDavDck7MWTlyx-eRAjm8")
dp = Dispatcher()

def  get_random_img():
    try:
        urls = media.get('images',[])
        print(urls)
        return random.choice(urls) if urls else None
    except Exception:
        return None

@dp.message(Command('start'))
async def cmd_start(message: types.message):
    await message.answer("Здарова")

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
    text = message.text.replace('/echo','').strip()
    if text:
        await message.answer(text)
    else:
        await message.answer('и че это щас было')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())