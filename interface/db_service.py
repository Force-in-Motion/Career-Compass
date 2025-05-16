from abc import ABC, abstractmethod


class ADBInit(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None

    @abstractmethod
    def _create_table(self, request):
        pass

    @abstractmethod
    def init_db(self):
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
    def get_password(self, *args) -> bool:
        pass

    @abstractmethod
    def get_email(self, *args) -> bool:
        pass

    @abstractmethod
    def get_way_notify(self, *args) -> bool:
        pass

    @abstractmethod
    def update_username(self, *args) -> bool:
        pass

    @abstractmethod
    def update_password(self, *args) -> bool:
        pass

    @abstractmethod
    def update_email(self, *args) -> bool:
        pass

    @abstractmethod
    def update_way_notify(self, *args) -> bool:
        pass

    @abstractmethod
    def delete_user(self, *args) -> bool:
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
    def del_vacancies(self) -> tuple[str]:
        pass



class AQueriesAdapter(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None

    @abstractmethod
    def add_query(self, *args) -> None:
        pass

    @abstractmethod
    def get_query(self) -> tuple[str]:
        pass

    @abstractmethod
    def del_query(self) -> tuple[str]:
        pass



class AFacade(ABC):
    def __init__(self, db_init: ADBInit, user_adapter: AUserAdapter, queries_adapter: AQueriesAdapter):
        self._db_init = db_init
        self._user_adapter = user_adapter
        self._queries_adapter = queries_adapter
        self._db_init.init_db()

    @abstractmethod
    def add_user(self, *args) -> None:
        pass

    @abstractmethod
    def get_all_username(self) -> tuple[str]:
        pass

    @abstractmethod
    def get_password(self, *args) -> bool:
        pass

    @abstractmethod
    def get_email(self, *args) -> bool:
        pass

    @abstractmethod
    def get_way_notify(self, *args) -> bool:
        pass

    @abstractmethod
    def update_username(self, *args) -> bool:
        pass

    @abstractmethod
    def update_password(self, *args) -> bool:
        pass

    @abstractmethod
    def update_email(self, *args) -> bool:
        pass

    @abstractmethod
    def update_way_notify(self, *args) -> bool:
        pass

    @abstractmethod
    def delete_user(self, *args) -> bool:
        pass

    @abstractmethod
    def add_vacancy(self, *args) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> tuple[str]:
        pass

    @abstractmethod
    def del_vacancies(self) -> tuple[str]:
        pass

    @abstractmethod
    def add_query(self, *args) -> None:
        pass

    @abstractmethod
    def get_query(self) -> tuple[str]:
        pass

    @abstractmethod
    def del_query(self) -> tuple[str]:
        pass