from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
btn1 = KeyboardButton('Запустить бота')
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1)
