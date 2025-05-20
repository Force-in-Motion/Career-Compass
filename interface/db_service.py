from abc import ABC, abstractmethod


class ADBInit(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None

    @abstractmethod
    def _create_table(self, query) -> None:
        pass

    @abstractmethod
    def init_db(self) -> None:
        pass




class AUserAdapter(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None

    @abstractmethod
    def add_user(self, *args) -> None:
        pass

    @abstractmethod
    def get_all_username(self) -> tuple[str]:
        pass

    @abstractmethod
    def get_userid_by_username_and_telegramid(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def get_password_by_username_and_telegramid(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def get_email_by_username_and_telegramid(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def get_way_notify_by_username_and_telegramid(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def update_username_by_password_and_telegramid(self, *args) -> None:
        pass

    @abstractmethod
    def update_password_by_username_and_telegramid(self, *args) -> None:
        pass

    @abstractmethod
    def update_email_by_username_and_telegramid(self, *args) -> None:
        pass

    @abstractmethod
    def update_way_notify_by_username_and_telegramid(self, *args) -> None:
        pass

    @abstractmethod
    def delete_user_by_username_and_telegramid(self, *args) -> None:
        pass



class AVacanciesAdapter(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None

    @abstractmethod
    def add_vacancy(self, *args) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> tuple[str]:
        pass

    @abstractmethod
    def del_vacancies(self) -> None:
        pass



class AQueriesAdapter(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None

    @abstractmethod
    def add_query_by_userid(self, *args) -> None:
        pass

    @abstractmethod
    def get_query_by_userid(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def update_query_by_userid(self, *args) -> None:
        pass

    @abstractmethod
    def del_query_by_userid(self, *args) -> None:
        pass



class AFacade(ABC):
    def __init__(self, db_init, user_adapter, queries_adapter, vacancies_adapter):
        self._db_init = db_init
        self._user_adapter = user_adapter
        self._queries_adapter = queries_adapter
        self._vacancies_adapter = vacancies_adapter
        self._db_init.init_db()

    @abstractmethod
    def add_user(self, *args) -> None:
        pass

    @abstractmethod
    def get_all_username(self) -> tuple[tuple[str]]:
        pass

    @abstractmethod
    def get_userid(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def get_password(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def get_email(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def get_way_notify(self, *args) -> tuple[str]:
        pass

    @abstractmethod
    def update_username(self, *args) -> None:
        pass

    @abstractmethod
    def update_password(self, *args) -> None:
        pass

    @abstractmethod
    def update_email(self, *args) -> None:
        pass

    @abstractmethod
    def update_way_notify(self, *args) -> None:
        pass

    @abstractmethod
    def delete_user(self, *args) -> None:
        pass

    @abstractmethod
    def add_vacancy(self, *args) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> tuple[str]:
        pass

    @abstractmethod
    def del_vacancies(self) -> None:
        pass

    @abstractmethod
    def add_query(self, *args) -> None:
        pass

    @abstractmethod
    def get_query(self) -> tuple[str]:
        pass

    @abstractmethod
    def update_query(self) -> None:
        pass

    @abstractmethod
    def del_query(self) -> None:
        pass