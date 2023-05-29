from aiogram import types, Dispatcher
from config import bot
from config import ADMIN,DICES
import random



async def pin(message: types.Message):
        if message.chat != 'private':
            if not message.reply_to_message:
                await message.answer('комнда должна быть ответом')
            else:
                await bot.pin_chat_message(message.chat.id, message.message_id)
        else:
            await message.answer('пиши в группе')

async def game(message: types.Message):
        if message.chat != 'private':
            if not message.from_user.id in ADMIN:
                await message.answer('ты не админ')
            else:
                await bot.send_dice(message.chat.id, emoji= random.choices(DICES))

        else:
            await message.answer('пиши в группе')


def register_handlers_admin(dp:Dispatcher):

    dp.register_message_handler(pin,commands= ['pin'])
    dp.register_message_handler(game,commands= ['game'])
