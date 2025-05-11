from abc import ABC, abstractmethod


class ADBUser(ABC):

    @abstractmethod
    def __init__(self):
        self._connect = None
        self._cursor = None
        self._create_table()

    @abstractmethod
    def _create_table(self) -> None:
        pass


    @abstractmethod
    def add_user(self, *args) -> None:
        pass


    @abstractmethod
    def get_all_names_users(self) -> tuple[str]:
        pass


    @abstractmethod
    def get_password_by_username_and_telegram_id(self, *args) -> bool:
        pass


    @abstractmethod
    def get_email_by_username_and_telegram_id(self, *args) -> bool:
        pass


    @abstractmethod
    def get_way_notify_by_username_and_telegram_id(self, *args) -> bool:
        pass


    @abstractmethod
    def update_username_by_password_and_telegram_id(self, *args) -> bool:
        pass


    @abstractmethod
    def update_password_by_username_and_telegram_id(self, *args) -> bool:
        pass


    @abstractmethod
    def update_email_by_username_and_telegram_id(self, *args) -> bool:
        pass


    @abstractmethod
    def update_way_notify_by_username_and_telegram_id(self, *args) -> bool:
        pass


    @abstractmethod
    def delete_user_by_username_and_telegram_id(self, *args) -> bool:
        pass