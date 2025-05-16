from logging import getLogger
from interface.db.user import AUserDataAccess
from service.db_service.sqlite.requests.user import user_request as ur
from tools.data_access import Connector as c

class UserAdapter(AUserDataAccess):
    def __init__(self):
        pass


    def add_user(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('add_user'), *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_all_username(self) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('get_all_user_name'))

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_password(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('get_password'), *args)

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)

    def get_email(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('get_email'), *args)

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_way_notify(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('get_way_notify'), *args)

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_username(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('update_username'), *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_password(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('update_password'), *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_email(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('update_email'), *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_way_notify(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('update_way_notify'), *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def delete_user(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get('del_user'), *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


