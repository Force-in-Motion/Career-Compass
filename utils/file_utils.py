
import json
import os
from pathlib import Path


class FileUtils:
    
    
    @staticmethod
    def get_token_path():
        return Path('src/telegram/settings/token.json').resolve()


    @staticmethod
    def get_db_path() -> str:
        """
        Создает относительный путь к файлу common_areas
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path_db = os.path.join(current_dir, '..', 'storage', 'database.db')

        return os.path.abspath(path_db)

    
    @staticmethod
    def get_token() -> str:
        """
        Получает токен по указанному пути
        :return: Токен в виде строки
        """
        with open(FileUtils.get_token_path(), 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['TOKEN']