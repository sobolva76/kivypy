# ниже указаны самое распространенное разрешение экрана на телефонах
from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '1')
# необходимые модули
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import gamebase, gamestart, gameend


class BaseScreens(ScreenManager):
    """ Класс определяющий скрины, в kv указываем подключаемые скрины"""


class NineGameSApp(App):
    """ Главный класс загрузки """


if __name__ == "__main__":
    NineGameSApp().run()