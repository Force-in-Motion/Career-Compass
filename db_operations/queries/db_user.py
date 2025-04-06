import sqlite3
from utils.file_utils import FileUtils as fu
from db_operations.requests.user import UserRequest as ur
from db_operations.queries.db_init import UserTable

class UserQueries:
    def __init__(self):
        self.__connect = sqlite3.connect(fu.get_db_path())
        self.__cursor = self.__connect.cursor()
        self.__user_table = UserTable()

    def add_user(self, name: str, password: str, telegram_id: int) -> None:
        """
        Добавляет в базу данных нового пользователя
        :param name: имя пользователя
        :param password: пароль пользователя
        :param telegram_id: telegram_id пользователя
        :return:
        """
        self.__cursor.execute(ur.add_user, (name, password, telegram_id))

        self.__connect.commit()

    def get_all_names_user(self) -> list[str]:
        """
        Возвращает все имена пользователей, хранящихся в базе данных
        :return: tuple[str]
        """
        self.__cursor.execute(ur.get_all_user_name)

        return self.__cursor.fetchall()

    def get_user_password(self, username):
        """
        Возвращает пароль пользователя, соответствующий его имени в базе данных
        :param username: имя пользователя
        :return:
        """
        self.__cursor.execute(ur.get_password, (username,))

        return self.__cursor.fetchall()