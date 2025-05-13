import requests
from bs4 import BeautifulSoup


class Vacancy:
    def __init__(self, title, company, link, salary=None):
        self.title = title
        self.company = company
        self.link = link
        self.salary = salary

    def __str__(self):
        salary_info = f'Зарплата: {self.salary}' if self.salary else 'Зарплата: Не указана'
        return f'Название: {self.title}\nКомпания: {self.company}\n{salary_info}\nСсылка: {self.link}'


class HHParser:
    def __init__(self, search_query, min_salary=None, max_salary=None, location=None, employment_type=None, experience=None):
        self.base_url = 'https://hh.ru/search/vacancy'
        self.search_query = search_query
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.location = location
        self.employment_type = employment_type
        self.experience = experience
        self.vacancies = []

    def fetch_vacancies(self):
        params = {
            'text': self.search_query,
            'salary': f'{self.min_salary}-{self.max_salary}' if self.min_salary and self.max_salary else None,
            'area': self.location,
            'employment': self.employment_type,
            'experience': self.experience,
            'page': 0
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            self.parse_vacancies(response.text)
        else:
            print(f'Ошибка при запросе: {response.status_code}')

    def parse_vacancies(self, html):
        soup = BeautifulSoup(html, 'lxml')
        vacancy_items = soup.find_all('div', class_='vacancy-serp-item')

        for item in vacancy_items:
            title_tag = item.find('a', class_='bloko-link')
            title = title_tag.text.strip() if title_tag else "Не указано"

            company_tag = item.find('div', class_='vacancy-serp-item__meta-info-company')
            company = company_tag.text.strip() if company_tag else "Не указано"

            link = title_tag['href'] if title_tag else "Не указано"

            salary_tag = item.find('span', class_='bloko-header-section-3')
            salary = salary_tag.text.strip() if salary_tag else None

            vacancy = Vacancy(title, company, link, salary)
            self.vacancies.append(vacancy)

    def display_vacancies(self):
        if not self.vacancies:
            print("Вакансии не найдены.")
            return

        for vacancy in self.vacancies:
            print(vacancy)
            print('-' * 40)


if __name__ == '__main__':

    # Словарь ID городов России
    location_id_map = {
        "Москва": 113,
        "Санкт-Петербург": 2,
        "Новосибирск": 4,
        "Екатеринбург": 5,
        "Нижний Новгород": 6,
        "Казань": 7,
        "Челябинск": 8,
        "Омск": 9,
        "Самара": 10,
        "Ростов-на-Дону": 11,
        "Уфа": 12,
        "Красноярск": 13,
        "Воронеж": 14,
        "Пермь": 15,
        "Волгоград": 16,
        "Краснодар": 17,
        "Тюмень": 18,
        "Ижевск": 19,
        "Барнаул": 20,
        "Ульяновск": 21,
        "Хабаровск": 22,
        "Ярославль": 23,
        # Добавьте другие города по мере необходимости.
    }

    search_query = input("Введите ключевые слова для поиска вакансий: ")
    min_salary = input("Введите минимальную зарплату (или оставьте пустым): ")
    max_salary = input("Введите максимальную зарплату (или оставьте пустым): ")

    location_input = input("Введите местоположение: ")
    location_id = location_id_map.get(location_input.strip(), None)

    employment_type_options = {
        'full': 'Полная занятость',
        'part': 'Частичная занятость',
        'remote': 'Удаленная работа'
    }

    print("Выберите тип занятости:")
    for key in employment_type_options.keys():
        print(f"{key}: {employment_type_options[key]}")

    employment_type_input = input("Введите тип занятости (full/part/remote или оставьте пустым): ")

    experience_options = {
        'noExperience': 'Без опыта',
        'between1And3': 'От года до трех лет',
        'between3And6': 'От трех до шести лет',
        'moreThan6': 'Более шести лет'
    }

    print("Выберите уровень опыта:")
    for key in experience_options.keys():
        print(f"{key}: {experience_options[key]}")

    experience_input = input("Введите уровень опыта (или оставьте пустым): ")

    parser = HHParser(
        search_query=search_query,
        min_salary=min_salary if min_salary else None,
        max_salary=max_salary if max_salary else None,
        location=location_id,
        employment_type=employment_type_input if employment_type_input in employment_type_options.keys() else None,
        experience=experience_input if experience_input in experience_options.keys() else None)

    parser.fetch_vacancies()
    parser.display_vacancies()
