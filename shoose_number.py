import random 
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN = '5164475581:AAHprXR3KKQzsZerMnIMcsigyxQCTvP6N7M'

bot = Bot( BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5

user = {'in_game':False,
        'secret_number':None,
        'attempts':None,
        'total_games':0,
        'wins':0}


def get_random_number() -> int:
    return random.randint(1,100)

@dp.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer("Hello, dear!\nWould you like to play?")


@dp.message(Command(commands='help'))
async def help_command(message:Message):
    await message.answer(
        f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
        f'попыток\n\nДоступные команды:\n/help - правила '
        f'игры и список команд\n/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n\nДавай сыграем?'
    )


@dp.message(Command(commands="stat"))
async def stat_command(message:Message):
    await message.answer(
        f'Attempts: {ATTEMPTS}\n'
        f'Total games: {user["total_games"]}\n'
        f'Wins: {user["wins"]}'
    )


@dp.message(Command(commands="cancel"))
async def cancel_command(message:Message):
    if user['in_game'] :
        user['in_game'] = False
        await message.answer(
            f'The game have been canceled'
        )
    else:
        await message.answer(
            f'You are not in the game\n'
            f'Do you want to play?'
        )

@dp.message(F.text.lower().in_(['yes', 'y', 'да', 'давай']))
async def start_game(message:Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS

        await message.answer(
            f'Game is begining!\n'
            f'Choose your destiny'
        )
    
    else:
        await message.answer(
            f'you are on the game\n'
            f'use /stat , /help or /cancel commands\n'
            f'or give me RIGHT number '
        )

    
    
@dp.message(F.text.lower().in_(["no", "нет", "не хочу"]))
async def refuse_command(message:Message):
    if not  user['in_game']:
        await message.answer(
            f'Ok. Press /start if you change your mind'
        )
    else:
        await message.answer(
            f'You on the game. \n You can only lose or win'
        )
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def the_game(message:Message):
    if user["in_game"]:
        if int(message.text) == int(user["secret_number"]):
            user["wins"] += 1
            user["total_games"] += 1
            user["in_game"] = False
            await message.answer(
                f'You are win \n'
                f'The number was {user["secret_number"]}\n'
                f'Do you wanna play the game again?'
            )
        elif int(message.text) > int(user["secret_number"]):
            user["attempts"] -= 1
            await message.answer(
                f'Your number is bigger tnen the NUMBER \n'
                f'Please try again'
                )
        elif int(message.text) < int(user["secret_number"]):
            user["attempts"] -= 1
            await message.answer(
                f'Your number is too less \n'
                f'Please try again'
                )
            
        if user["attempts"] <= 0:
            user["in_game"] = False
            await message.answer(
                f'Unfortunatly yo are lose\n'
                f'The number was {user["secret_number"]}\n'
                f'You can try again /start'
            )
    else:
        await message.answer("You are not in the game. \nDo you wanna /start ?")


dp.message()
async def process_other_message(message:Message):
    if user["in_game"]:
        await message.answer("We in the game\n Put the number from 1 t0 100")
    else:
        await message.answer("I cant understand you.\n Do you wanna /start the game?")

if __name__ == '__main__':
    dp.run_polling(bot)

