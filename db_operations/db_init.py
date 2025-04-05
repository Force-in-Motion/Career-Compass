import sqlite3

from db_operations.requests.create_tables import CreateTables as ct
from utils.file_utils import FileUtils as fu


class UserTable:

    def __init__(self):
        self.__connect = sqlite3.connect(fu.get_db_path())
        self.__cursor = self.__connect.cursor()
        self.__create_user_table()

    def __create_user_table(self) -> None:
        """
        Создает таблицу для хранения данных пользователей
        :return: None
        """
        self.__cursor.execute(ct.add_user_table)

        self.__connect.commit()


class VacanciesTable:

    def __init__(self):
        self.__connect = sqlite3.connect(fu.get_db_path())
        self.__cursor = self.__connect.cursor()
        self.__create_vacancies_table()

    def __create_vacancies_table(self) -> None:
        """
        Создает таблицу для хранения данных вакансии
        :return: None
        """
        self.__cursor.execute(ct.add_vacancies_table)

        self.__connect.commit()


class QueriesTable:

    def __init__(self):
        self.__connect = sqlite3.connect(fu.get_db_path())
        self.__cursor = self.__connect.cursor()
        self.__create_queries_table()

    def __create_queries_table(self) -> None:
        """
        Создает таблицу для хранения данных запросов
        :return: None
        """
        self.__cursor.execute(ct.add_queries_table)

        self.__connect.commit()

