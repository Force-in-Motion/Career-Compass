from aiogram.utils.keyboard import InlineKeyboardBuilder


class KBInline:

    @staticmethod
    def create_authorization_buttons():
        """
        Создает кнопки для регистрации или авторизации пользователя
        :return: None
        """
        kb = InlineKeyboardBuilder()

        kb.button(text='Регистрация', callback_data='registration')
        kb.button(text='Авторизация', callback_data='authorization')

        kb.adjust(2)

        return kb.as_markup(resize_keyboard=True)


    @staticmethod
    def create_main_menu_kb():
        """
        Создает кнопку для возврата в главное меню
        :return: None
        """
        kb = InlineKeyboardBuilder()

        kb.button(text='Главное меню', callback_data='main_menu')

        kb.adjust(1)

        return kb.as_markup(resize_keyboard=True)

