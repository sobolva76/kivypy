# File name: bets.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from kivy.properties import NumericProperty, StringProperty

from kivy.config import Config

from kivy.lang import Builder

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')

Builder.load_file('widgets.kv')


class Bet(BoxLayout):
    player_name = StringProperty('')
    bet_amount = NumericProperty(0)
    max_bet_amount = NumericProperty(0)
    player_group = StringProperty('')


class BetsScreen(Screen):
    pass


class BetsApp(App):
    def build(self):
        return BetsScreen()
    

if __name__ == '__main__':
    BetsApp().run()