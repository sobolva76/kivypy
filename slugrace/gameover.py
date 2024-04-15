# File name: gameover.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from kivy.config import Config

from kivy.lang import Builder

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')

Builder.load_file('widgets.kv')


class GameoverScreen(Screen):
    pass


class GameoverApp(App):
    def build(self):
        return GameoverScreen()
    

if __name__ == '__main__':
    GameoverApp().run()