import os
from contextlib import asynccontextmanager

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
    @asynccontextmanager
    async def sqlite_connect(query: str, params: tuple = (), commit: bool = True):
        """
        Асинхронный контекстный менеджер для выполнения SQL-запросов с параметрами.

        :param query: SQL-запрос в виде строки
        :param params: кортеж параметров для запроса (по умолчанию пустой)
        :param commit: выполнять ли commit для изменений в БД (по умолчанию True)
        :yield: курсор для работы с результатами запроса
        :raises RuntimeError: если произошла ошибка при выполнении запроса
        """
        connect = await aiosqlite.connect(FileUtils.get_path())
        cursor = await connect.cursor()

        try:
            if params:
                await cursor.execute(query, params)
            else:
                await cursor.execute(query)
            yield cursor

            if commit:
                await connect.commit()

        except Exception as e:
            await connect.rollback()
            raise RuntimeError(f"Ошибка при выполнении запроса: {e}")

        finally:
            await cursor.close()
            await connect.close()

