# File name: main.py

import kivy
from kivy.app import App

from kivy.uix.screenmanager import ScreenManager

from kivy.config import Config

from kivy.lang import Builder

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '1')

Builder.load_file('settings.kv')
Builder.load_file('race.kv')
Builder.load_file('gameover.kv')


class SlugraceScreenManager(ScreenManager):
    pass


class SlugraceApp(App):
    def build(self):
        return SlugraceScreenManager()


if __name__ == '__main__':
    SlugraceApp().run()