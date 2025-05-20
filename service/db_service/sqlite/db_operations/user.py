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


    async def add_user(self, *args) -> None:
        """
        Добавляет данные пользователя в базу в случае успешного выполнения запроса
        :param args: данные пользователя
        :return:
        """
        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('add_user'), *args)

            await self._connect.commit()

            logger.debug('add_user успешно добавила пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_all_username(self) -> tuple[str]:
        """
        Получает данные пользователя из базы в случае успешного выполнения запроса
        :return: имена всех пользователей
        """
        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_all_user_name'))

            result = await self._cursor.fetchall()

            logger.debug('get_all_username вернула %s', result)

            return result

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_userid_by_username_and_telegramid(self, *args) -> tuple[str]:
        """
        Получает id пользователя из базы в случае успешного выполнения запроса
        :param args: пароль конкретного пользователя
        :return:
        """
        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_id'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_password вернула %s', result)

            return result


        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_password_by_username_and_telegramid(self, *args) -> tuple[str]:
        """
        Получает пароль пользователя из базы в случае успешного выполнения запроса
        :param args: пароль конкретного пользователя
        :return:
        """
        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_password'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_password вернула %s',result)

            return result


        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)

    async def get_email_by_username_and_telegramid(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_email'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_email вернула %s',result)

            return result


        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_way_notify_by_username_and_telegramid(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_way_notify'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_way_notify вернула %s', result)

            return result

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_username_by_password_and_telegramid(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_username'), *args)

            await self._connect.commit()

            logger.debug('update_username успешно обновила имя пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_password_by_username_and_telegramid(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_password'), *args)

            await self._connect.commit()

            logger.debug('update_password успешно обновила пароль пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_email_by_username_and_telegramid(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_email'), *args)

            await self._connect.commit()

            logger.debug('update_email успешно обновила email пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_way_notify_by_username_and_telegramid(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_way_notify'), *args)

            await self._connect.commit()

            logger.debug('update_way_notify успешно обновила способ уведомления пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def delete_user_by_username_and_telegramid(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('del_user'), *args)

            await self._connect.commit()

            logger.debug('delete_user успешно удалила пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


