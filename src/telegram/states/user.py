from aiogram.fsm.state import StatesGroup, State


class Entrance(StatesGroup):
    """
    Содержит состояние, при котором пользователь делает выбор зарегистрироваться или авторизоваться
    """
    wait_entrance = State()


class UserRegistration(StatesGroup):
    """
    Содержит состояния, при которых пользователь проходит регистрацию
    """
    wait_reg_name = State()
    wait_reg_pass = State()


class UserAuthorization(StatesGroup):
    """
    Содержит состояния, при которых пользователь проходит авторизацию
    """
    wait_auth_name = State()
    wait_auth_pass = State()


class UserParams(StatesGroup):
    wait_email = State()
    wait_notification = State()