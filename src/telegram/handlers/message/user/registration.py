import asyncio

from aiogram import F
from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.model.user import UserData
from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.states.user import UserRegistration as ur
from utils.processing import ProcessingData as pd

router = Router()


@router.message(StateFilter(ur.wait_reg_name), F.text)
async def input_username_handler(message: types.Message, state: FSMContext) -> None:
    if not pd.check_username_in_db(message.text):
        await state.update_data(telegram_id=message.from_user.id, username=message.text)
        await message.reply(om.success_reg_name)
        await message.answer(om.reg_pass)
        await state.set_state(ur.wait_reg_pass)
    else:
        await message.reply(om.err_reg_name)


@router.message(StateFilter(ur.wait_reg_pass), F.text)
async def input_password_handler(message: types.Message, state: FSMContext) -> None:
    await state.update_data(password=message.text)
    await message.reply(om.success_reg_pass)
    data = await state.get_data()
    user = UserData(username=data.get('username'), password=data.get('password'), telegram_id=data.get('telegram_id'))
    user.save_user_in_db()
    await asyncio.sleep(2)
    await message.answer(om.success_reg_user)
    await state.clear()
