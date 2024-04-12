# File name: results.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
from kivy.properties import NumericProperty, StringProperty

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')


class Result(BoxLayout):
    player_name = StringProperty('')
    money_before = NumericProperty(0)
    bet_amount = NumericProperty(0)
    slug_name = StringProperty('')
    result_info = StringProperty('')
    gain_or_loss = NumericProperty(0)
    current_money = NumericProperty(0)
    odds = NumericProperty(0)


class ResultsScreen(BoxLayout):
    pass

class ResultsApp(App):
    def build(self):
        return ResultsScreen()

if __name__ == '__main__':
    ResultsApp().run()