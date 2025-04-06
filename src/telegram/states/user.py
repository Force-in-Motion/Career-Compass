from aiogram.fsm.state import StatesGroup, State


class Entrance(StatesGroup):
    wait_entrance = State()


class UserRegistration(StatesGroup):
    wait_reg_name = State()
    wait_reg_pass = State()


class UserAuthorization(StatesGroup):
    wait_auth_name = State()
    wait_auth_pass = State()


class UserParams(StatesGroup):
    wait_email = State()
    wait_notification = State()