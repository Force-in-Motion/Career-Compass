
queries_request = {
                    'add_query': """
                        INSERT INTO Queries (user_id, city, profession, salary_min, experience_level, date_added)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """,

                    'get_query': """
                        SELECT * FROM Queries WHERE user_id = ?
                        """,

                    'update_query': """
                        UPDATE Queries SET city = ?, profession = ?, salary_min = ?, experience_level = ?, date_added = ?
                        WHERE user_id = ?
                        """,

                    'del_query': """
                        DELETE FROM Queries WHERE user_id = ?
                        """
}