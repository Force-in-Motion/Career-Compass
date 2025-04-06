
class UserRequest:
    """
    Содержит запросы для работы с таблицей пользователей
    """
    get_all_user_name = """
        SELECT username From User
        """

    add_user = """
        INSERT INTO User (username, password, telegram_id) VALUES (?, ?, ?)
        """

    get_password = """
        SELECT password FROM User WHERE username = ?
    """