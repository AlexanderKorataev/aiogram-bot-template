# импортируем состояния из библиотеки для создания класса форм
from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    url = State()
