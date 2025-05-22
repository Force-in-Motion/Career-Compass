from logging import getLogger

from interface.db_service import AUserAdapter
from service.db_service.sqlite.requests.user import user_request as ur
from tools.data_access import Connector as c

logger = getLogger(__name__)

class UserAdapter(AUserAdapter):
    """ Осуществляет доступ к данным пользователей """

    def __init__(self):
        super().__init__()
        self._connect = None
        self._cursor = None


    async def add_user(self, *args) -> bool:
        """
        Добавляет данные пользователя в базу в случае успешного выполнения запроса
        :param args: данные пользователя
        :return:
        """
        async with c.sqlite_connect(ur.get('add_user'), *args) as self._cursor:

            logger.debug('add_user успешно добавила пользователя')

            return True



    async def get_all_username(self) -> tuple[tuple[str]]:
        """
        Получает данные пользователя из базы в случае успешного выполнения запроса
        :return: имена всех пользователей
        """
        async with c.sqlite_connect(ur.get('get_all_user_name'), commit=False) as self._cursor:

            result = await self._cursor.fetchall()

            logger.debug('get_all_username вернула %s', result)



    async def get_userid_by_username_and_telegramid(self, *args) -> tuple[str]:
        """
        Получает id пользователя из базы в случае успешного выполнения запроса
        :param args: пароль конкретного пользователя
        :return:
        """
        async with c.sqlite_connect(ur.get('get_id'), *args, commit=False) as self._cursor:

            result = await self._cursor.fetchone()

            logger.debug('get_password вернула %s', result)

            return result


    async def get_password_by_username_and_telegramid(self, *args) -> tuple[str]:
        """
        Получает пароль пользователя из базы в случае успешного выполнения запроса
        :param args: пароль конкретного пользователя
        :return:
        """
        async with c.sqlite_connect(ur.get('get_password'), *args, commit=False) as self._cursor:

            result = await self._cursor.fetchone()

            logger.debug('get_password вернула %s',result)

            return result


    async def get_email_by_username_and_telegramid(self, *args) -> tuple[str]:

        async with c.sqlite_connect(ur.get('get_email'), *args, commit=False) as self._cursor:

            result = await self._cursor.fetchone()

            logger.debug('get_email вернула %s',result)

            return result


    async def get_way_notify_by_username_and_telegramid(self, *args) -> tuple[str]:

        async with c.sqlite_connect(ur.get('get_way_notify'), *args, commit=False) as self._cursor:

            result = await self._cursor.fetchone()

            logger.debug('get_way_notify вернула %s', result)

            return result


    async def update_username_by_password_and_telegramid(self, *args) -> bool:

        async with c.sqlite_connect(ur.get('update_username'), *args) as self._cursor:

            logger.debug('update_username успешно обновила имя пользователя')

            return True


    async def update_password_by_username_and_telegramid(self, *args) -> bool:

        async with c.sqlite_connect(ur.get('update_password'), *args) as self._cursor:

            logger.debug('update_password успешно обновила пароль пользователя')

            return True


    async def update_email_by_username_and_telegramid(self, *args) -> bool:

        async with c.sqlite_connect(ur.get('update_email'), *args) as self._cursor:

            logger.debug('update_email успешно обновила email пользователя')

            return True


    async def update_way_notify_by_username_and_telegramid(self, *args) -> bool:

        async with c.sqlite_connect(ur.get('update_way_notify'), *args) as self._cursor:

            logger.debug('update_way_notify успешно обновила способ уведомления пользователя')

            return True


    async def delete_user_by_username_and_telegramid(self, *args) -> bool:

        async with c.sqlite_connect(ur.get('del_user'), *args) as self._cursor:

            logger.debug('delete_user успешно удалила пользователя')

            return True



