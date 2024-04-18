# File name: main.py

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import NumericProperty
from kivy.config import Config
from kivy.lang import Builder

from player import Player

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '1')

Builder.load_file('settings.kv')
Builder.load_file('race.kv')
Builder.load_file('gameover.kv')
Builder.load_file('widgets.kv')
Builder.load_file('slug.kv')


class Game(ScreenManager):
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()

    number_of_players = NumericProperty(2)
    players = [player1, player2]


class SlugraceApp(App):
    def build(self):
        return Game()


if __name__ == '__main__':

    from kivy.core.window import Window
    Window.clearcolor = (1, 1, .8, 1)
    SlugraceApp().run()