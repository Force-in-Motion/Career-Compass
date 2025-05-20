from interface.db_service import AFacade


class DatabaseFacade(AFacade):
    """ Предоставляет API сервиса работы с базой данных """

    def __init__(self, db_init, user_adapter, queries_adapter, vacancies_adapter):
        super().__init__(db_init, user_adapter, queries_adapter, vacancies_adapter)
        self._db_init = db_init
        self._user_adapter = user_adapter
        self._queries_adapter = queries_adapter
        self._vacancies_adapter = vacancies_adapter
        self._db_init.init_db()


# Работа с данными пользователя

    async def add_user(self, username: str, password: str, telegram_id: int) -> None:
        """
        Добавляет пользователя в базу данных
        :param username: имя пользователя
        :param password: пароль пользователя
        :param telegram_id: телеграм id пользователя
        :return: None
        """
        await self._user_adapter.add_user(username, password, telegram_id)


    async def get_all_username(self) -> tuple[tuple[str]]:
        """
        Возвращает имена всех пользователей системы из базы данных
        :return: tuple[tuple[str]]
        """
        return await self._user_adapter.get_all_username()


    async def get_userid(self, username: str, telegram_id: int) -> tuple[str]:
        """
        Возвращает id пользователя из базы данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: tuple[str]
        """
        return await self._user_adapter.get_userid_by_username_and_telegramid(username, telegram_id)


    async def get_password(self, username: str, telegram_id: int) -> tuple[str]:
        """
        Возвращает пароль пользователя из базы данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: tuple[str]
        """
        return await self._user_adapter.get_password_by_username_and_telegramid(username, telegram_id)


    async def get_email(self, username: str, telegram_id: int) -> tuple[str]:
        """
        Возвращает электронную почту пользователя из базы данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: tuple[str]
        """
        return await self._user_adapter.get_email_by_username_and_telegramid(username, telegram_id)


    async def get_way_notify(self, username: str, telegram_id: int) -> tuple[str]:
        """
        Возвращает способ уведомления пользователя из базы данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: tuple[str]
        """
        return await self._user_adapter.get_way_notify_by_username_and_telegramid(username, telegram_id)


    async def update_username(self, password: str, telegram_id: int) -> None:
        """
        Обновляет имя пользователя в базе данных
        :param password: пароль пользователя
        :param telegram_id: телеграм id пользователя
        :return: None
        """
        await self._user_adapter.update_username_by_password_and_telegramid(password, telegram_id)


    async def update_password(self, username: str, telegram_id: int) -> None:
        """
        Обновляет пароль пользователя в базе данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: None
        """
        await self._user_adapter.update_password_by_username_and_telegramid(username, telegram_id)


    async def update_email(self, username: str, telegram_id: int) -> None:
        """
        Обновляет электронную почту пользователя в базе данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: None
        """
        await self._user_adapter.update_email_by_username_and_telegramid(username, telegram_id)


    async def update_way_notify(self, username: str, telegram_id: int) -> None:
        """
        Обновляет способ уведомления пользователя в базе данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: None
        """
        await self._user_adapter.update_way_notify_by_username_and_telegramid(username, telegram_id)


    async def delete_user(self, username: str, telegram_id: int) -> None:
        """
        Удаляет пользователя из базы данных
        :param username: имя пользователя
        :param telegram_id: телеграм id пользователя
        :return: None
        """
        await self._user_adapter.delete_user_by_username_and_telegramid(username, telegram_id)


# Работа с данными вакансий

    async def add_vacancy(self, vacancy) -> None:
        await self._vacancies_adapter.add_vacancy(vacancy)


    async def get_vacancies(self):
        await self._vacancies_adapter.get_vacancies()


    async def del_vacancies(self) -> None:
        pass


#  Работа с параметрами запросов

    async def add_query(self, *args) -> None:
        self._queries_adapter.add_query_by_user_id(args)


    async def get_query(self):
        return await self._queries_adapter.get_query_by_userid()


    def update_query(self) -> None:
        pass


    async def del_query(self) -> None:
        pass


