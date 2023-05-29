from config import dp,bot
from aiogram import types, Dispatcher
from keibort import klient_kb


async def quiz_2(call: types.CallbackQuery):

    question = 'куда?'
    answers = ['в космос ', 'на луну']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=3,
        reply_markup=klient_kb.markup2
    )

async def quiz_3(call: types.CallbackQuery):

    question = 'на чем?'
    answers = ['на лосях', 'на машине']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=3,
        reply_markup=klient_kb.markup3
    )


def register_callbek_hansdlers(dp:Dispatcher):
    dp.register_callback_query_handler(quiz_2,text='button')
    dp.register_callback_query_handler(quiz_3,text='button')
