from mailbox import Message

from aiogram import F
from aiogram import Router, types
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext

from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.states.user import Entrance as et
from src.telegram.states.user import UserRegistration as us

router = Router()


@router.message(StateFilter(et.user_entrance), Command('reg'))
async def command_reg_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает команду reg для входа в состояние регистрации пользователя
    :param message: сообщение пользователя
    :param state: состояние начала регистрации
    :return: None
    """
    await state.set_state(us.user_name)
    await message.answer(om.input_name)
