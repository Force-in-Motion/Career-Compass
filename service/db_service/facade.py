from interface.db_service import AFacade


class DatabaseFacade(AFacade):
    """ Предоставляет апи сервиса работы с базой данных """

    def __init__(self, db_init, user_adapter, queries_adapter, vacancies_adapter):
        super().__init__(db_init, user_adapter, queries_adapter, vacancies_adapter)
        self._db_init = db_init
        self._user_adapter = user_adapter
        self._queries_adapter = queries_adapter
        self._vacancies_adapter = vacancies_adapter
        self._db_init.init_db()


    async def add_user(self, *args) -> None:
        """
        Добавляет пользователя в базу данных
        :param args: данные пользователя
        :return:None
        """
        await self._user_adapter.add_user(args)


    async def get_all_username(self):
        """
        Возвращает имена всех пользователей системы
        :return:
        """
        return await self._user_adapter.get_all_username()



    async def get_password(self, *args):
        """
        Возвращает пароль пользователя
        :param args: username, telegram_id
        :return:
        """
        return await self._user_adapter.get_password_by_username_and_telegramid(args)


    async def get_email(self, *args):
        return await self._user_adapter.get_email_by_username_and_telegramid(args)


    async def get_way_notify(self, *args):
        return await self._user_adapter.get_way_notify_by_username_and_telegramid(args)


    async def update_username(self, *args) -> None:
        await self._user_adapter.update_username_by_password_and_telegramid(args)


    async def update_password(self, *args) -> None:
        await self._user_adapter.update_password_by_username_and_telegramid(args)


    async def update_email(self, *args) -> None:
        await self._user_adapter.update_email_by_username_and_telegramid(args)


    async def update_way_notify(self, *args) -> None:
        await self._user_adapter.update_way_notify_by_username_and_telegramid(args)


    async def delete_user(self, *args) -> None:
        await self._user_adapter.delete_user_by_username_and_telegramid(args)


    async def add_vacancy(self, *args) -> None:
        await self._vacancies_adapter.add_vacancy(args)


    async def get_vacancies(self):
        await self._vacancies_adapter.get_vacancies()


    async def del_vacancies(self) -> None:
        pass


    async def add_query(self, *args) -> None:
        self._queries_adapter.add_query_by_user_id(args)


    async def get_query(self):
        return await self._queries_adapter.get_query_by_userid()


    async def del_query(self) -> None:
        pass


