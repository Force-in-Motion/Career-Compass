from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext


from src.telegram.output.output_mess import OutputMessage as om
from src.telegram.keyboard.inline import KBInline as kbi
from src.telegram.states.user import Entrance as et

router = Router()


@router.message(StateFilter(et.wait_entrance), F.text)
async def incorrect_input_auth_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает неожиданный текст, полученный от пользователя во время регистрации или авторизации
    Удаляет предыдущее сообщение бота по id и последнее сообщение пользователя, тем самым очищая чат
    :param message: сообщение пользователя
    :param state: состояние FSMContext
    :return: None
    """
    data = await state.get_data()
    mess_id = data.get('mess_id')
    await message.chat.delete_message(mess_id)
    mess = await message.answer(om.err_choice_auth, reply_markup=kbi.create_authorization_kb_inline())
    await state.update_data(mess_id=mess.message_id)
    await message.delete()
