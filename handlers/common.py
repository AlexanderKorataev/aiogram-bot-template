"""Сommon handlers and registration"""
from aiogram import types
from aiogram.dispatcher import Dispatcher
import os
from messages import MESSAGES
from keyboards import set_link_keyboard, update_link_keyboard
from states import Form
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher

class CommonHandlers:
    """Сommon handlers"""

    async def start_command(message: types.Message, dp: Dispatcher) -> None:
        """
        Handler of the /start command

        Args:
            message (types.Message): Instance of the Message class.
        """
        await dp.bot.send_message(
                message.chat.id,
                MESSAGES['start'].format(message.from_user.username),
                reply_markup=set_link_keyboard
            )
            # Add the user ID to the environment variable
        if(not os.environ.get('USER_IDS')):
            user_ids = []
        else:
            user_ids = os.environ.get('USER_IDS').split(',')
        if str(message.chat.id) not in user_ids:
            user_ids.append(str(message.chat.id))
            os.environ['USER_IDS'] = ','.join(user_ids)
            await message.answer(
        'Let\'s get started!🔥'
        )

    async def help_command(message: types.Message) -> None: 
        """
        Handler of the /help command

        Args:
            message (types.Message): Instance of the Message class.
        """

        await message.answer(
            'We\'ll be there soon🆘'
            )
        
    async def cancel_command(message: types.Message, state: FSMContext) -> None: 
        """
        Handler of the /help command

        Args:
            message (types.Message): Instance of the Message class.
        """
        current_state = await state.get_state()
        if current_state is None:
            return
        else:
            await state.finish()
            await message.answer(
                MESSAGES['cancel']
            )

    async def set_link(message: types.Message) -> None:

        await Form.url.set()
        await message.answer(
                MESSAGES['set_link']
        )


    async def unknown(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['url'] = message.text
        # Save the URL to an environment variable
        os.environ['URL'] = data['url']
        await state.finish()
        await message.answer(
            MESSAGES['link_updated']
            )

def register_client_handlers(dp: Dispatcher) -> None:
    """
    Registration of common handlers

    Args:
        dp (Dispatcher): Instance of the Dispatcher class.
    """
    dp.register_message_handler(CommonHandlers.start_command, commands=['start'])
    dp.register_message_handler(CommonHandlers.help_command, commands=['help'])
    dp.register_message_handler(CommonHandlers.cancel_command, commands=['cancel'])
    dp.register_message_handler(CommonHandlers.unknown)