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


    async def add_query_by_userid(self, *args) -> bool:
        """
        Добавляет параметры запроса пользователя в базу если запрос выполнился успешно
        :param args: user_id, city, profession, salary_min, experience_level
        :return: None
        """
        with c.sqlite_connect(qr.get('add_query'), *args) as self._cursor:

            logger.debug('add_query_by_userid успешно добавила параметры поиска работы пользователя')

            return True


    async def get_query_by_userid(self, *args) -> tuple[str]:
        """
        Получает параметры запроса пользователя из базы если запрос выполнился успешно
        :param args: user_id
        :return: tuple[str]
        """
        with c.sqlite_connect(qr.get('get_query'), *args, commit=False) as self._cursor:

            result = await self._cursor.fetchone()

            logger.debug('get_query_by_userid вернула %s', result)

            return result


    async def update_query_by_userid(self, *args) -> bool:
        """
        Обновляет параметры запроса пользователя в базе если запрос выполнился успешно
        :param args: user_id, city, profession, salary_min, experience_level
        :return: None
        """
        with c.sqlite_connect(qr.get('update_query'), *args) as self._cursor:

            logger.debug('update_query_by_userid успешно обновила параметры поиска работы пользователя')

            return True


    async def del_query_by_userid(self, *args) -> bool:
        """
        Удаляет параметры запроса пользователя из базы если запрос выполнился успешно
        :param args: user_id
        :return: None
        """
        with c.sqlite_connect(qr.get('del_query'), *args) as self._cursor:

            logger.debug('del_query_by_userid успешно удалила параметры поиска работы пользователя')

            return True