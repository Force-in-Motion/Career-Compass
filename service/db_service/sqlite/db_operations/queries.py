from logging import getLogger
from interface.db_service import AQueriesAdapter
from service.db_service.sqlite.requests.user import user_request as ur
from tools.data_access import Connector as c

logger = getLogger(__name__)

class QueriesAdapter(AQueriesAdapter):

    def __init__(self):
        self._connect = None
        self._cursor = None


    def add_query(self, *args) -> None:

        try:
            self._connect, self._cursor = c.sqlite_connect(*args)

            self._connect.commit()

            logger.debug('Данных запроса пользователя успешно добавлены')

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении данных запроса пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_query(self) -> tuple[str]:
        try:
            self._connect, self._cursor = c.sqlite_connect()

            logger.debug('Данных запроса пользователя успешно добавлены')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении данных запроса пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)

    def del_query(self) -> None:

        try:
            self._connect, self._cursor = c.sqlite_connect()

            self._connect.commit()

            logger.debug('Данных запроса пользователя успешно удалены')

        except Exception as e:
            raise RuntimeError(f"Ошибка при удалении данных запроса пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)