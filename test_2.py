from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = '5164475581:AAHprXR3KKQzsZerMnIMcsigyxQCTvP6N7M'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет, чмо")

@dp.message()
async def answer_message(message:Message):
    await message.answer(text="you so pity with your text: " + message.text)

if __name__ == '__main__':
    dp.run_polling(bot)

    

print("bon jour!")