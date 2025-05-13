
vacancies_request = {
                    'add_vacancy': """ INSERT INTO Vacancies (name, salary, company, description, link, city, date_added)
                     VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,

                    'get_vacancies': """ SELECT * FROM Vacancies JOIN Queries
                     ON Vacancies.city = Queries.city AND Vacancies.salary >= Queries.salary
                     AND Vacancies.name_profession LIKE '%' || Queries.name_profession || '%'
                     """

}