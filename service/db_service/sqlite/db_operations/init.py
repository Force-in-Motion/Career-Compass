from interface.db.adapter.init import ADBInit
from service.db_service.sqlite.requests.table import creating_tables as ct
from tools.data_access import Connector as c


class DBInitAdapter(ADBInit):
    """ Объект содержащий методы работы с базой данных """

    def __init__(self):
        self._connect = None
        self._cursor = None


    def _create_table(self, query) -> None:
        """
        Создает таблицу в базе данных
        :param query: принимает запрос
        :return: None
        """
        try:
            self._cursor, self._connect = c.sqlite_connect(ct.get(query))

        except Exception as e:
            raise RuntimeError(f"Ошибка при создании таблицы: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def init_db(self) -> None:
        """
        Инициализирует создание базы данных
        :return: None
        """
        for table in ct.values():
            self._create_table(table)






