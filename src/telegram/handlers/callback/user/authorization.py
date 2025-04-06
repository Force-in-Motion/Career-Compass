from aiogram import F
from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.states.user import Entrance as et
from src.telegram.states.user import UserAuthorization as ua

router = Router()

@router.callback_query(StateFilter(et.wait_entrance), F.data)
async def authorization_callback_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает клик по кнопке "Авторизация", удаляет сообщение с кнопками (регистрация, авторизация),
    запрашивает ввод имени пользователя и меняет состояние
    :param callback: кол бэк функцию
    :param state: текущее состояние
    :return: None
    """
    await callback.message.delete()
    await callback.message.answer(om.auth_name)
    await state.set_state(ua.wait_auth_name)
    await callback.answer()