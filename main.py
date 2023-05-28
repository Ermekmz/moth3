from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = config('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['quiz'])
async def quiz (message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Next', callback_data='button')
    markup.add(button)
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
        reply_markup=markup
    )

@dp.callback_query_handler(text='button')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Next', callback_data='button2')
    markup.add(button)
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
        reply_markup=markup
    )
@dp.message_handler(commands=['meme'])
async def photo(message: types.Message):
    photo = open('media/unnamed.png','rb')
    await bot.send_photo(message.from_user.id, photo= photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await message.answer(int(message.text)**2)
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates= True)

