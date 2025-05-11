import sqlite3

from interface.db import ADBUser
from service.db_service.db_operations.requests.tables import CreateTables as ct
from tools.data_access import SqLiteConnector as sqlc


class DBOperations(ADBUser):
    """ Объект содержащий методы работы с базой данных """

    def __init__(self):
        self._create_table()


    def _create_table(self) -> None | Exception:
        """
        Создает таблицу погоды в базе данных
        """
        try:
            self._cursor, self._connect = sqlc.connect(create_table)

        except Exception as e:
            raise RuntimeError(f"Ошибка при создании таблицы: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)


    def add_record(self, *args) -> None | Exception:
        """
        Добавляет запись в базу данных
        :param args: параметры для SQL-запроса добавления записи
        """
        try:
            self._cursor, self._connect = dbc.connect(add_record, args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Невозможно добавить запись: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)


    def get_records(self) -> None | Exception:
        """
        Получает все записи из базы данных
        :return: Кортеж записей
        """
        try:
            self._cursor, self._connect = dbc.connect(get_record)
            return self._cursor.fetchall()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении записей: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)


    def update_record(self, *args) -> None | Exception:
        """
        Обновляет таблицу базы данных
        :return: None | Exception
        """
        try:
            self._cursor, self._connect = dbc.connect(update_record, args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при обновлении таблицы: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)



    def close_connect(self, cursor, connect) -> None:
        """
        Закрывает соединение с базой данных
        :param cursor: объект курсора
        :param connect: объект соединения
        :return: None
        """
        if connect:
            cursor.close()
            connect.close()
