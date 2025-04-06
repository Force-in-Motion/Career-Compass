from aiogram import F
from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.states.user import Entrance as et
from src.telegram.states.user import UserRegistration as us

router = Router()


@router.callback_query(StateFilter(et.wait_entrance), F.data == 'registration')
async def registration_callback_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает клик по кнопке "Регистрация", удаляет сообщение с кнопками (регистрация, авторизация),
    запрашивает ввод имени пользователя и меняет состояние
    :param callback: кол бэк функцию
    :param state: текущее состояние
    :return: None
    """
    await callback.message.delete()
    await callback.message.answer(om.reg_name)
    await state.set_state(us.wait_reg_name)
    await callback.answer()


