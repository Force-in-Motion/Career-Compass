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


    async def add_vacancy(self, **args) -> bool:
        """
        Добавляет все данные о конкретной вакансии в базу данных
        :param args: принимает данные о вакансии
        :return: bool
        """
        with c.sqlite_connect(v.get('add_vacancy'), *args) as self._cursor:

            logger.debug('add_vacancy успешно добавила данные о желаемой вакансии:', *args)

            return True


    async def get_vacancies(self, *args) -> tuple[str]:

        with c.sqlite_connect(v.get('get_vacancies'), *args) as self._cursor:

            result = await self._cursor.fetchone()

            logger.debug('get_vacancies вернула вакансии для конкретного пользователя', result)

            return result



    async def del_vacancies(self, *args) -> bool:

        with c.sqlite_connect(v.get('get_vacancies'), *args) as self._cursor:

            logger.debug('del_vacancies удалила вакансии для конкретного пользователя', *args)

            return True