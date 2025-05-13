
user_request = {
                'get_all_user_name': """
                    SELECT username From User
                    """,

                'add_user': """
                    INSERT INTO User (username, password, telegram_id) VALUES (?, ?, ?)
                    """,

                'get_password': """
                    SELECT password FROM User WHERE username = ? and telegram_id = ?
                    """,

                'get_email': """
                    SELECT email FROM User WHERE username = ? and telegram_id = ?
                    """,

                'get_way_notify': """
                    SELECT notifications FROM User WHERE username = ? and telegram_id = ?
                    """,

                'update_username': """
                    UPDATE User SET username WHERE password = ? and telegram_id = ?
                    """,

                'update_password': """
                    UPDATE User SET password WHERE username = ? and telegram_id = ?
                    """,

                'update_email': """
                    UPDATE User SET email WHERE username = ? and telegram_id = ?
                    """,

                'update_way_notify': """
                    UPDATE User SET notifications WHERE username = ? and telegram_id = ?
                    """,

                'del_user': """
                    DELETE FROM User WHERE username = ? and telegram_id = ?
                    """

    }
