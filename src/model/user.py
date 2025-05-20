from datetime import datetime

from pydantic import EmailStr, BaseModel

from service.db_service.sqlite.db_operations.user import UserAdapter

ua = UserAdapter()

class User(BaseModel):
        username: str
        password: str
        telegram_id: int
        email: EmailStr | None
        notifications: str | None







class Vacancy(BaseModel):
    profession: str
    requirements: str
    description: str
    salary: int
    company: str
    link: str
    city: str
    date_added: datetime