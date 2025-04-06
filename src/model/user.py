from  pydantic import EmailStr
from db_operations.queries.db_user import UserQueries

uq = UserQueries()

class UserData:
    def __init__(self, username: str, password: str, telegram_id: int, email: EmailStr = None, notifications: str = None):
        self.__username = username
        self.__password = password
        self.__telegram_id = telegram_id
        self.__email = email
        self.__notifications = notifications


    def save_user_in_db(self) -> None:
        """
        Сохраняет в базе данных нового пользователя
        :return: None
        """
        uq.add_user(self.__username, self.__password, self.__telegram_id)

