from interface.db.vacancies import AVacanciesDataAccess
from service.db_service.sqlite.requests.vacancies import vacancies_request as v
from tools.data_access import Connector as c


class VacancyAdapter(AVacanciesDataAccess):

    def __init__(self):
        self._connect = None
        self._cursor = None


    def add_vacancy(self, *args) -> None:
        try:
            self._cursor, self._connect = c.sqlite_connect(v.get('add_vacancy'), *args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении вакансии: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)


    def get_vacancies(self) -> tuple[str]:
        try:
            self._cursor, self._connect = c.sqlite_connect(v.get('get_vacancies'))

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении вакансий: {e}")

        finally:
            c.sqlite_close(self._connect, self._cursor)

