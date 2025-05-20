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
        self._user_adapter.add_user(args)


    async def get_all_username(self):
        """
        Возвращает имена всех пользователей системы
        :return:
        """
        all_username = self._user_adapter.get_all_username()
        return all_username


    async def get_password(self, *args):
        """
        Возвращает пароль пользователя
        :param args: username, telegram_id
        :return:
        """
        password = self._user_adapter.get_password(args)
        return password


    async def get_email(self, *args):
        email = self._user_adapter.get_email(args)
        return email


    async def get_way_notify(self, *args):
        way_notify = self._user_adapter.get_way_notify(args)
        return way_notify


    async def update_username(self, *args) -> None:
        self._user_adapter.update_username(args)


    async def update_password(self, *args) -> None:
        self._user_adapter.update_password(args)


    async def update_email(self, *args) -> None:
        self._user_adapter.update_email(args)


    async def update_way_notify(self, *args) -> None:
        self._user_adapter.update_way_notify(args)


    async def delete_user(self, *args) -> None:
        self._user_adapter.delete_user(args)


    async def add_vacancy(self, *args) -> None:
        self._vacancies_adapter.add_vacancy(args)


    async def get_vacancies(self):
        self._vacancies_adapter.get_vacancies()


    async def del_vacancies(self) -> None:
        pass


    async def add_query(self, *args) -> None:
        pass

    async def get_query(self):
        pass

    async def del_query(self) -> None:
        pass


