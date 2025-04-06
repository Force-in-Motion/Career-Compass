import asyncio

from aiogram import F
from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.states.user import UserAuthorization as ua
from utils.processing import ProcessingData as pd

router = Router()


@router.message(StateFilter(ua.wait_auth_name), F.text)
async def input_username_handler(message: types.Message, state: FSMContext) -> None:
    if pd.check_username_in_db(message.text):
        await message.reply(om.success_auth_name)
        await message.answer(om.auth_pass)
        await state.set_state(ua.wait_auth_pass)
        await state.update_data(username=message.text)
    else:
        await message.reply(om.err_auth_name)


@router.message(StateFilter(ua.wait_auth_pass), F.text)
async def input_password_handler(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    username = data.get('username')

    if message.text == pd.get_user_password(username):
        await state.update_data(password=message.text)
        await message.reply(om.success_auth_pass)
        await asyncio.sleep(2)
        await message.answer(om.success_auth_user)
        await state.clear()
    else:
        await message.reply(om.err_auth_pass)
