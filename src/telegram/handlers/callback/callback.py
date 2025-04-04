from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram import Router, types
from aiogram import F

from src.telegram.keyboard.inline import KBInline as kbi
from src.telegram.states.user import UserRegistration as us


router = Router()

@router.callback_query(F.data == 'main_menu')
async def return_to_main_menu_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.answer('Вы возвращены в главное меню')






@router.callback_query(StateFilter(None), F.data == 'registration')
async def registration_callback_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.delete()
    await callback.message.answer('Введите имя пользователя\n', reply_markup=kbi.create_main_menu_kb())
    await state.set_state(us.user_name)
    await callback.answer()

