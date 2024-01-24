from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F


BOT_TOKEN = '5164475581:AAHprXR3KKQzsZerMnIMcsigyxQCTvP6N7M'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def reply_photo(message:Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

async def reply_voice(message:Message):
    await message.answer_voice(message.voice.file_id)

async def process_start_command(message: Message):
    await message.answer("Привет, чмо")


async def send_echo(message:Message):
    try:
        print(message.model_dump_json(indent=4, exclude_none=True))
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="unsuportable type of message")

@dp.message(Command(commands=["help"]))
async def process_help_command(message:Message):
    await message.answer("Бог тебе в помощь")


async def process_in_command(message:Message):
    await message.answer( "роса вам в очи")


async def answer_message(message:Message):
    await message.answer(text="you so peez ty with your text: " + message.text)





# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_in_command, Command(commands='in'))
dp.message.register(reply_photo, F.content_type==ContentType.PHOTO)
dp.message.register(reply_voice, F.voice)

dp.message.register(send_echo)


#dp.message.register(process_in_command, Command(commands=['in']))

if __name__ == '__main__':
    dp.run_polling(bot)

    


print("bon jour!")