import asyncio

from aiogram import Bot, Dispatcher

from src.telegram.handlers.callback import callback as cal
from src.telegram.handlers.command import command as cm
from src.telegram.handlers.text_mess import text_mess as tm
from utils.file_utils import FileUtils as fu


async def main() -> None:

    bot = Bot(fu.get_token())

    dp = Dispatcher()

    dp.include_routers(cm.router, cal.router, tm.router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)





if __name__ == '__main__':
    asyncio.run(main())