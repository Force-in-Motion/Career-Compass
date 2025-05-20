from logging import getLogger
from interface.db_service import AUserAdapter
from service.db_service.sqlite.requests.user import user_request as ur
from tools.data_access import Connector as c

logger = getLogger(__name__)

class UserAdapter(AUserAdapter):
    def __init__(self):
        super().__init__()
        self._connect = None
        self._cursor = None


    async def add_user(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('add_user'), *args)

            await self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_all_username(self) -> tuple[str]:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_all_user_name'))

            result = await self._cursor.fetchall()

            logger.debug('get_all_username вернула %s', result)

            return result

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_password(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_password'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_password вернула %s',result)

            return result


        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)

    async def get_email(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_email'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_email вернула %s',result)

            return result


        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_way_notify(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('get_way_notify'), *args)

            result = await self._cursor.fetchone()

            logger.debug('get_way_notify вернула %s', result)

            return result

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_username(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_username'), *args)

            await self._connect.commit()

            logger.debug('update_username успешно обновила имя пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_password(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_password'), *args)

            await self._connect.commit()

            logger.debug('update_password успешно обновила пароль пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_email(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_email'), *args)

            await self._connect.commit()

            logger.debug('update_email успешно обновила email пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def update_way_notify(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('update_way_notify'), *args)

            await self._connect.commit()

            logger.debug('update_way_notify успешно обновила способ уведомления пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def delete_user(self, *args) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(ur.get('del_user'), *args)

            await self._connect.commit()

            logger.debug('delete_user успешно удалила пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


