from interface.db.user import AUserDataAccess
from service.db_service.sqlite.requests.user import UserRequest as ur
from tools.data_access import Connector as c

class SqLiteUserAdapter(AUserDataAccess):
    def __init__(self):
        pass


    def add_user(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.add_user, *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_all_username(self) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get_all_user_name)

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_password(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get_password, *args)

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении списка имен всех пользователей: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)

    def get_email(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get_email, *args)

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_way_notify(self, *args) -> tuple[str]:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.get_way_notify, *args)

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_username(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.update_username, *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_password(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.update_password, *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_email(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.update_email, *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def update_way_notify(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.update_way_notify, *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def delete_user(self, *args) -> None:

        try:
            self._cursor, self._connect = c.sqlite_connect(ur.del_user, *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении email пользователя: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


