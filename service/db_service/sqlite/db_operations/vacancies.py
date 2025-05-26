from logging import getLogger

from interface.db_service import AVacanciesAdapter
from service.db_service.sqlite.requests.vacancies import vacancies_request as v
from tools.data_access import Connector as c

logger = getLogger(__name__)

class VacancyAdapter(AVacanciesAdapter):

    def __init__(self):
        super().__init__()
        self._connect = None
        self._cursor = None


    async def add_vacancy(self, **kwargs) -> None:

        try:
            self._cursor, self._connect = await c.sqlite_connect(v.get('add_vacancy'), **kwargs)

            self._connect.commit()

            logger.debug('add_vacancy успешно добавила данные о желаемой вакансии')

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении вакансии: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def get_vacancies(self) -> tuple[str]:
        try:
            self._cursor, self._connect = await c.sqlite_connect(v.get('get_vacancies'))

            result = await self._cursor.fetchone()

            logger.debug('get_vacancies вернула вакансии для конкретного пользователя')

            return result

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении вакансий: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)


    async def del_vacancies(self) -> None:
        try:
            self._cursor, self._connect = await c.sqlite_connect(v.get('get_vacancies'))

            self._connect.commit()

            logger.debug('del_vacancies удалила вакансии для конкретного пользователя')

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении вакансий: {e}")

        finally:
            await c.sqlite_close(self._connect, self._cursor)