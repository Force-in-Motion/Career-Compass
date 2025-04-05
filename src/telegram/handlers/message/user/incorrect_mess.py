from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message

from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.states.user import Entrance as et

router = Router()


@router.message(StateFilter(et.user_entrance), F.text)
async def incorrect_input_handler(message: Message) -> None:
    """
    Обрабатывает неожиданный текст, полученный от пользователя во время регистрации или авторизации
    :param message: сообщение пользователя
    :return: None
    """
    await message.answer(om.err_choice_auth)
