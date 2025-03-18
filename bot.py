import asyncio
from aiogram import Bot,Dispatcher
from src.utils.file_utils import FileUtils as fu


async def main() -> None:

    bot = Bot(fu.get_token())

    dp = Dispatcher()

    # dp.include_routers()

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())