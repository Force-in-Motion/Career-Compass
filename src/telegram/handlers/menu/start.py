from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.telegram.keyboard.inline import KBInline as kbi
from src.telegram.keyboard.reply import KBReply as kbr
from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.states.user import Entrance as et

router = Router()


@router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает команду start и выводит приветственное сообщение
    :param message: сообщение пользователя
    :param state: состояние регистрации или авторизации пользователя
    :return:
    """
    await state.clear()
    await message.answer(om.opening_greeting)
    mess = await message.answer(om.btn_selection, reply_markup=kbi.create_authorization_kb_inline())
    await state.set_state(et.wait_entrance)
    await state.update_data(mess_id=mess.message_id)

