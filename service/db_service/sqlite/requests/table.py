
    creating_tables = {
                'user_table': """
                    CREATE TABLE IF NOT EXISTS User (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    telegram_id INTEGER NOT NULL,
                    email TEXT,
                    notifications TEXT
                    )
                    """,

                'vacancies_table': """
                    CREATE TABLE IF NOT EXISTS Vacancies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_profession TEXT NOT NULL,
                    salary INTEGER NOT NULL,
                    company TEXT NOT NULL,
                    description TEXT NOT NULL,
                    link TEXT NOT NULL,
                    city TEXT NOT NULL,
                    date_added TEXT NOT NULL
                    )
                    """,

                'queries_table': """
                    CREATE TABLE IF NOT EXISTS Queries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    city TEXT NOT NULL,
                    name_profession TEXT NOT NULL,
                    salary INTEGER NOT NULL,
                    date_request TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES Users (id)
                    )
                    """
    }

