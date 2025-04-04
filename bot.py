import asyncio
from aiogram import Bot, Dispatcher
from src.telegram.handlers import command
from utils.file_utils import FileUtils as fu
from src.telegram.handlers.command import command
from src.telegram.handlers.callback import callback



async def main() -> None:

    bot = Bot(fu.get_token())

    dp = Dispatcher()

    dp.include_routers(command.router,
                                callback.router
                       )

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())