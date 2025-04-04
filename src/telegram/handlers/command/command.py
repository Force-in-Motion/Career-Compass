
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.telegram.keyboard.inline import KBInline as kbi
from src.telegram.output.output_mess import OutputMessage as om

router = Router()


@router.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    """
    Обрабатывает команду start и выводит приветственное сообщение
    :param message: сообщение пользователя
    :return: None
    """
    await message.answer(om.opening_greeting)
    await message.answer(om.authorization_mess, reply_markup=kbi.create_authorization_buttons())


@router.message(Command('menu'))
async def main_menu_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает команду возврата в главное меню, сбрасывает все state
    :param message: сообщение пользователя
    :param state: состояние
    :return: None
    """
    await state.clear()
    await message.answer(om.return_to_main_menu)


