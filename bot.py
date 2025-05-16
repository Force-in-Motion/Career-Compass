import asyncio

from aiogram import Bot, Dispatcher

from src.telegram.settings.token_reader import setting
from tools.logger import logger_config

from src.telegram.handlers.menu.start import router as greeting
from src.telegram.handlers.menu.main_menu import router as main_menu
from src.telegram.handlers.message.user.registration import router as user_reg_message
from src.telegram.handlers.callback.user.registration import router as user_reg_callback
from src.telegram.handlers.message.user.authorization import router as user_auth_message
from src.telegram.handlers.callback.user.authorization import router as user_auth_callback
from src.telegram.handlers.message.error.incorrect_auth import router as incorrect_mess_entrance

logger = logger_config()

async def main() -> None:

    bot = Bot(setting.TOKEN.get_secret_value())

    dp = Dispatcher()

    dp.include_routers(greeting,
                                main_menu,
                                user_reg_message,
                                user_reg_callback,
                                user_auth_message,
                                user_auth_callback,
                                incorrect_mess_entrance
                       )
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
