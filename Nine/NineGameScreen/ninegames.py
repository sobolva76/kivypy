from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock
import gamebase, gamestart, gameend

# ниже указаны самое распространенное разрешение экрана на телефонах
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '1')


class BaseScreens(ScreenManager):
    """ Класс определяющий скрины, м kv указываем подключаемые скрины"""
    print("SM")

class NineGameSApp(App):
    """ Главный класс загрузки """
    print("SM-App")


if __name__ == "__main__":
    NineGameSApp().run()