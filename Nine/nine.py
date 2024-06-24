import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivy.lang import Builder


Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '1')

Builder.load_file('nineGameV2.kv')


class Nine(ScreenManager):
    """ класс основного экрана"""


class NineApp(App):
    def build(self):
        nine_game = Nine()
        return nine_game
    

if __name__ == '__main__':
    NineApp().run()