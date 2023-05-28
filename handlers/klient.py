from aiogram import types, Dispatcher

from config import dp,bot
from keibort import klient_kb




async def photo(message: types.Message):
    photo = open('media/unnamed.png','rb')
    await bot.send_photo(message.from_user.id, photo= photo)


async def quiz (message: types.Message):

    question = 'как ты?'
    answers = ['хорошо', 'плохо']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=3,
        reply_markup=klient_kb.markup1
    )

def register_handlers_klient(dp:Dispatcher):
    dp.register_message_handler(photo, commands=['meme'])
    dp.register_message_handler(quiz, commands=['quiz'])
