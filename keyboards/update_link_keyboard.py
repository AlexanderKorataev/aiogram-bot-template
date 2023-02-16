# импортируем типы из библиотеки aiogram
from aiogram import types

# создаем все кнопки, которые буду располагаться на клавиатурах
update_link_button = types.KeyboardButton('Обновить ссылку для поиска')


update_link_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
update_link_keyboard.add(update_link_button)
