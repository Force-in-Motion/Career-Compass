from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from src.telegram.output.output_mess import OutputMessage as om

router = Router()


@router.message(F.text.lower() == 'главное меню')
async def main_menu_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает полученный текст возврата в главное меню, сбрасывает все стейты
    :param message: Принимает сообщение пользователя
    :param state: Принимает состояние
    :return: None
    """
    await state.clear()
    await message.answer(om.return_to_main_menu)
