import os
import aiosqlite



class FileUtils:
    """ Класс, содержащий служебные методы получения пути и доступа к данным """


    @staticmethod
    def get_path(*args) -> str:
        """
        Создает относительный путь к файлу
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, *args)

        return os.path.abspath(path)




class Connector:

    @staticmethod
    async def sqlite_connect(query: str, params: tuple = ()):
        """
        Выполняет SQL-запрос с параметрами (если есть) и возвращает курсор.

        :param query: SQL-запрос в виде строки
        :param params: кортеж параметров для запроса (по умолчанию пустой)
        :return: sqlite3.connect, sqlite3.cursor
        """
        connect = await aiosqlite.connect(FileUtils.get_path())
        cursor = await connect.cursor()

        try:
            if params:
                await cursor.execute(query, params)
            else:
                await cursor.execute(query)

            return cursor, connect

        except Exception as e:
            raise RuntimeError(f"Ошибка при выполнении запроса: {e}")


    @staticmethod
    async def sqlite_close(connect, cursor) -> None:
        """
        Закрывает соединение если оно открыто
        :param connect: объект соединения
        :param cursor: объект курсора
        :return:None
        """
        if connect:
            await connect.close()
            await cursor.close()
