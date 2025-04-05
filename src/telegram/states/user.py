from aiogram.fsm.state import StatesGroup, State


class Entrance(StatesGroup):
    user_entrance = State()


class UserRegistration(StatesGroup):
    user_name = State()
    user_password = State()
    user_email = State()
    notification = State()


class UserAuthorization(StatesGroup):
    user_name = State()
    user_password = State()
