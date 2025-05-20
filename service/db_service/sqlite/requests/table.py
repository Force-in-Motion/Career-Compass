
    creating_tables = {

                'user_table': """
                    CREATE TABLE IF NOT EXISTS User (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    telegram_id INTEGER UNIQUE NOT NULL,
                    email TEXT,
                    notifications TEXT,
                    is_active INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                    """,

                'vacancies_table': """
                    CREATE TABLE IF NOT EXISTS Vacancies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    profession TEXT NOT NULL,
                    requirements TEXT,
                    description TEXT NOT NULL,
                    salary INTEGER NOT NULL,
                    company TEXT NOT NULL,
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
                    profession TEXT NOT NULL,
                    salary_min INTEGER NOT NULL,
                    experience_level TEXT,
                    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE
                    )
                    """
    }

