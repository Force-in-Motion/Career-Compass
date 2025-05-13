from abc import ABC, abstractmethod


class AVacanciesDataAccess(ABC):

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
