# импортируем типы из библиотеки aiogram
from aiogram import types


# создаем кнопку, которая будет располагаться на клавиатуре
set_link_button = types.KeyboardButton('Задать ссылку для поиска')

set_link_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
set_link_keyboard.add(set_link_button)
