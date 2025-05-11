from abc import ABC, abstractmethod


class AUserDataAccess(ABC):

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