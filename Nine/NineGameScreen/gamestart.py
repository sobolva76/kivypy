from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Blok(Widget):
    """ Класс постоянных блоков блоков - стены, пол, потолок, и нижняя кайма """ 
    print("blok-start")

class GameStartScreen(Screen):
    """ Главный класс игры """
    print("screen-start")

    # функция запускается призагрузке скрина
    def on_enter(self, *args):
        print("on_enter")

    # функция запускается после выхода из скрина
    def on_leave(self, *args):
        print("on_leavel")


class GamestartApp(App):
    print("App-start")