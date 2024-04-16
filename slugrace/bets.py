# File name: bets.py

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from kivy.properties import NumericProperty, StringProperty


class Bet(BoxLayout):
    player_name = StringProperty('')
    bet_amount = NumericProperty(0)
    max_bet_amount = NumericProperty(0)
    player_group = StringProperty('')


class BetsScreen(Screen):
    pass