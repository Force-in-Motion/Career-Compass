import json
import os
import sqlite3
from config.path import *





class FileUtils:
    """ Класс, содержащий служебные методы получения пути и доступа к данным """


    @staticmethod
    def get_path(*args) -> str:
        """
        Создает относительный путь к файлу
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, *args)

        return os.path.abspath(path)

    
    @staticmethod
    def get_token() -> str:
        """
        Получает токен по указанному пути
        :return: Токен в виде строки
        """
        with open(FileUtils.get_path(token), 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['TOKEN']




class Connector:

    @staticmethod
    def sqlite_connect(query: str, params: tuple = ()):
        """
        Выполняет SQL-запрос с параметрами (если есть) и возвращает курсор.

        :param query: SQL-запрос в виде строки
        :param params: кортеж параметров для запроса (по умолчанию пустой)
        :return: sqlite3.Cursor
        """
        connect = sqlite3.connect(FileUtils.get_path())
        cursor = connect.cursor()

        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor, connect

        except Exception as e:
            raise RuntimeError(f"Ошибка при выполнении запроса: {e}")


    @staticmethod
    def sqlite_close(connect, cursor) -> None:
        """
        Закрывает соединение если оно открыто
        :param connect: объект соединения
        :param cursor: объект курсора
        :return:None
        """
        if connect:
            connect.close()
            cursor.close()
