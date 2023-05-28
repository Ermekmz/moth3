from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup1 = InlineKeyboardMarkup()
button = InlineKeyboardButton('Next', callback_data='button')
markup1.add(button)

markup2 = InlineKeyboardMarkup()
button = InlineKeyboardButton('Next', callback_data='button2')
markup2.add(button)

markup3 = InlineKeyboardMarkup()
button = InlineKeyboardButton('Next', callback_data='button3')
markup3.add(button)
