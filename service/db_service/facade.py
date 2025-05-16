from service.db_service.sqlite.db_operations.user import UserAdapter


class DatabaseFacade(ABC):
    def __init__(self, db_init, user_adapter, queries_adapter):
        self._db_init = db_init
        self._user_adapter = user_adapter
        self._queries_adapter = queries_adapter
        self._db_init.init_db()

    def add_user(self, *args) -> None:
        self._user_adapter.add_user(args)

    def get_all_username(self) -> tuple[str]:
        pass

    def get_password(self, *args) -> bool:
        pass

    def get_email(self, *args) -> bool:
        pass

    def get_way_notify(self, *args) -> bool:
        pass

    def update_username(self, *args) -> bool:
        pass

    def update_password(self, *args) -> bool:
        pass

    def update_email(self, *args) -> bool:
        pass

    def update_way_notify(self, *args) -> bool:
        pass

    def delete_user(self, *args) -> bool:
        pass

    def add_vacancy(self, *args) -> None:
        pass

    def get_vacancies(self) -> tuple[str]:
        pass

    def del_vacancies(self) -> tuple[str]:
        pass

    def add_query(self, *args) -> None:
        pass

    def get_query(self) -> tuple[str]:
        pass

    def del_query(self) -> tuple[str]:
        pass


