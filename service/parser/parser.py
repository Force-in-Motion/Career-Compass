import asyncio
import logging
from contextlib import asynccontextmanager
from typing import Optional, Dict, List
from urllib.parse import urlencode

import aiosqlite
import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@asynccontextmanager
async def sqlite_connect(query: str, params: tuple = (), commit: bool = True):
    """
    Асинхронный контекстный менеджер для выполнения SQL-запросов.
    """
    connect = await aiosqlite.connect("vacancies.db")
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


async def init_db():
    """
    Инициализация базы данных для хранения вакансий.
    """
    query = """
    CREATE TABLE IF NOT EXISTS vacancies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        requirements TEXT,
        salary TEXT,
        company TEXT,
        link TEXT UNIQUE
    )
    """
    async with sqlite_connect(query, commit=True) as cursor:
        logger.debug("Таблица vacancies создана или уже существует")


class VacancyParser:
    def __init__(self):
        self.base_url = "https://hh.ru/search/vacancy"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }

    async def fetch_page(self, url: str) -> Optional[str]:
        """
        Асинхронный запрос страницы.
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                logger.debug(f"Успешный запрос: {url}, статус: {response.status_code}")
                return response.text
            except httpx.HTTPError as e:
                logger.error(f"Ошибка при запросе страницы {url}: {e}")
                return None

    async def parse_vacancy_page(self, url: str) -> Optional[Dict]:
        """
        Парсинг страницы конкретной вакансии.
        """
        html = await self.fetch_page(url)
        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")

        try:
            title = soup.select_one("h1[data-qa='vacancy-title']").text.strip() if soup.select_one(
                "h1[data-qa='vacancy-title']") else "Не указано"
            description = soup.select_one("div[data-qa='vacancy-description']").text.strip() if soup.select_one(
                "div[data-qa='vacancy-description']") else "Не указано"
            requirements = soup.select_one("div[data-qa='vacancy-requirements']").text.strip() if soup.select_one(
                "div[data-qa='vacancy-requirements']") else "Не указано"
            salary = soup.select_one("span[data-qa='vacancy-salary']").text.strip() if soup.select_one(
                "span[data-qa='vacancy-salary']") else "Не указано"
            company = soup.select_one("span[data-qa='company-name']").text.strip() if soup.select_one(
                "span[data-qa='company-name']") else "Не указано"

            return {
                "title": title,
                "description": description,
                "requirements": requirements,
                "salary": salary,
                "company": company,
                "link": url
            }
        except Exception as e:
            logger.error(f"Ошибка при парсинге вакансии {url}: {e}")
            return None

    async def save_vacancy(self, vacancy: Dict):
        """
        Сохранение вакансии в базу данных.
        """
        query = """
        INSERT OR IGNORE INTO vacancies (title, description, requirements, salary, company, link)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            vacancy["title"],
            vacancy["description"],
            vacancy["requirements"],
            vacancy["salary"],
            vacancy["company"],
            vacancy["link"]
        )
        try:
            async with sqlite_connect(query, params, commit=True) as cursor:
                logger.debug(f"Вакансия сохранена: {vacancy['title']}")
        except RuntimeError as e:
            logger.error(f"Ошибка при сохранении вакансии: {e}")

    async def search_vacancies(self, keywords: str, location: str = "", salary_min: Optional[int] = None,
                               employment_type: str = "", experience: str = "", max_pages: int = 1) -> List[Dict]:
        """
        Поиск вакансий по заданным параметрам.
        """
        # Преобразование location в код региона (пример для Москвы)
        area_mapping = {"Москва": "1", "Санкт-Петербург": "2"}  # Дополните словарь
        area = area_mapping.get(location, "")

        params = {
            "text": keywords,
            "area": area,
            "salary": salary_min if salary_min else "",
            "employment": employment_type,
            "experience": experience,
            "page": 0
        }

        vacancies = []
        async with httpx.AsyncClient() as client:
            for page in range(max_pages):
                params["page"] = page
                url = f"{self.base_url}?{urlencode(params)}"
                logger.debug(f"Запрос страницы: {url}")

                html = await self.fetch_page(url)
                if not html:
                    continue

                soup = BeautifulSoup(html, "html.parser")
                vacancy_cards = soup.select("div[data-qa='vacancy-serp__vacancy']")  # Обновлённый селектор

                if not vacancy_cards:
                    logger.debug(f"Вакансии не найдены на странице {page}")
                    break

                for card in vacancy_cards:
                    link_elem = card.select_one("a[data-qa='vacancy-serp__vacancy-title']")
                    if link_elem and link_elem.get("href"):
                        vacancy_url = link_elem.get("href")
                        vacancy_data = await self.parse_vacancy_page(vacancy_url)
                        if vacancy_data:
                            vacancies.append(vacancy_data)
                            await self.save_vacancy(vacancy_data)
                        await asyncio.sleep(1)  # Задержка для избежания блокировки

        return vacancies


async def main():
    """
    Пример использования парсера.
    """
    await init_db()
    parser = VacancyParser()
    vacancies = await parser.search_vacancies(
        keywords="Python разработчик",
        location="Москва",
        salary_min=100000,
        employment_type="Полный",
        experience="3 года",
        max_pages=2
    )
    logger.info(f"Найдено {len(vacancies)} вакансий")
    for vacancy in vacancies:
        logger.info(f"Вакансия: {vacancy['title']}, Компания: {vacancy['company']}, Ссылка: {vacancy['link']}")


if __name__ == "__main__":
    asyncio.run(main())