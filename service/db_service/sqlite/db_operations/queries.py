from logging import getLogger

from interface.db_service import AQueriesAdapter
from service.db_service.sqlite.requests.queries import queries_request as qr
from tools.data_access import Connector as c

logger = getLogger(__name__)


class QueriesAdapter(AQueriesAdapter):
    """ Осуществляет доступ к данным параметров запроса пользователей """

    def __init__(self):
        self._connect = None
        self._cursor = None


    async def add_query_by_userid(self, *args) -> None:
        """
        Добавляет параметры запроса пользователя в базу если запрос выполнился успешно
        :param args: user_id, city, profession, salary_min, experience_level
        :return: None
        """
        try:
            self._connect, self._cursor = await c.sqlite_connect(qr.get('add_query'), *args)

            await self._connect.commit()

            logger.debug('add_query_by_userid успешно добавила параметры поиска работы пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении данных запроса пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_query_by_userid(self, *args) -> tuple[str]:
        """
        Получает параметры запроса пользователя из базы если запрос выполнился успешно
        :param args: user_id
        :return: tuple[str]
        """
        try:
            self._connect, self._cursor = await c.sqlite_connect(qr.get('get_query'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_query_by_userid вернула %s', result)

            return result

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении данных запроса пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)



    async def update_query_by_userid(self, *args) -> None:
        """
        Обновляет параметры запроса пользователя в базе если запрос выполнился успешно
        :param args: user_id, city, profession, salary_min, experience_level
        :return: None
        """
        try:
            self._connect, self._cursor = await c.sqlite_connect(qr.get('update_query'), *args)

            await self._connect.commit()

            logger.debug('update_query_by_userid успешно обновила параметры поиска работы пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при удалении данных запроса пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def del_query_by_userid(self, *args) -> None:
        """
        Удаляет параметры запроса пользователя из базы если запрос выполнился успешно
        :param args: user_id
        :return: None
        """
        try:
            self._connect, self._cursor = await c.sqlite_connect(qr.get('del_query'), *args)

            await self._connect.commit()

            logger.debug('del_query_by_userid успешно удалила параметры поиска работы пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при удалении данных запроса пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)