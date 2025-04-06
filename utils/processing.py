from db_operations.queries.db_user import UserQueries

uq = UserQueries()

class ProcessingData:

    @staticmethod
    def check_username_in_db(username) -> bool:
        """
        Проверяет наличие полученного имени в списке имен базы данных
        :return:
        """
        names = [item[0] for item in uq.get_all_names_user()]

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

        return uq.get_user_password(username)[0][0]
