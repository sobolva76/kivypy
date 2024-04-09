# File name: gameover.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')


class GameoverScreen(BoxLayout):
    pass


class GameoverApp(App):
    def build(self):
        return GameoverScreen()
    

if __name__ == '__main__':
    GameoverApp().run()