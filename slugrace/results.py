# File name: results.py

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty


class Result(BoxLayout):
    player_name = StringProperty('')
    money_before = NumericProperty(0)
    bet_amount = NumericProperty(0)
    slug_name = StringProperty('')
    result_info = StringProperty('')
    gain_or_loss = NumericProperty(0)
    current_money = NumericProperty(0)
    odds = NumericProperty(0)


class ResultsScreen(Screen):
    pass