from aiogram import F
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.telegram.output.output_mess import OutputMessage as om

router = Router()


@router.callback_query(F.data == 'main_menu')
async def return_to_main_menu_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает клик по кнопке возврата в главное меню
    :param callback: кол бэк функцию
    :param state: текущее состояние
    :return: None
    """
    await state.clear()
    await callback.message.answer(om.return_to_main_menu)


@router.message(F.text.lower() == 'главное меню')
async def return_to_main_menu_message(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает полученное сообщение пользователя возврата в главное меню, сбрасывает все state
    :param message: сообщение пользователя
    :param state: текущее состояние
    :return: None
    """
    await state.clear()
    await message.answer(om.return_to_main_menu)


@router.message(Command('menu'))
async def return_to_main_menu_command(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает команду возврата в главное меню, сбрасывает все state
    :param message: сообщение пользователя
    :param state: состояние
    :return: None
    """
    await state.clear()
    await message.answer(om.return_to_main_menu)
