from service.db_service.facade import DatabaseFacade
from service.db_service.sqlite.db_operations.init import ADBInit
from service.db_service.sqlite.db_operations.queries import QueriesAdapter
from service.db_service.sqlite.db_operations.user import UserAdapter
from service.db_service.sqlite.db_operations.vacancies import VacancyAdapter

dbf = DatabaseFacade(ADBInit, UserAdapter, QueriesAdapter, VacancyAdapter)


class ProcessingData:

    @staticmethod
    async def check_username_in_db(username) -> bool:
        """
        Вызывает метод работы с BD для получения данных, содержащий все имена зарегистрированных пользователей
        :return: bool
        """
        names = [item[0] for item in await dbf.get_all_username()]

        if username in names:
            return True

        return False


    @staticmethod
    def get_user_password(username) -> str:
        """
        Вызывает метод работы с BD для получения данных, содержащих пароль пользователя, соответствующий его имени
        :param username: имя пользователя
        :return: пароль в виде строки
        """
        return dbf.get_user_password(username)[0][0]
