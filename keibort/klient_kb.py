from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

markup1 = InlineKeyboardMarkup()
button = InlineKeyboardButton('Next', callback_data='button')
markup1.add(button)

markup2 = InlineKeyboardMarkup()
button = InlineKeyboardButton('Next', callback_data='button2')
markup2.add(button)

markup3 = InlineKeyboardMarkup()
button = InlineKeyboardButton('Next', callback_data='button3')
markup3.add(button)

cancle_markup = ReplyKeyboardMarkup().add(KeyboardButton('cancle'))

back = KeyboardButton('Backend')
front = KeyboardButton('Frontend')
uxui = KeyboardButton('UX-UI')
android = KeyboardButton('Android')
ios = KeyboardButton('IOS')
napr_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back,front,uxui,android,ios,KeyboardButton('cancle'))

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(KeyboardButton('да'),KeyboardButton('нет'))

