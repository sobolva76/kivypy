# File name: race.py

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty, StringProperty

from kivy.lang import Builder

Builder.load_file('bets.kv')
Builder.load_file('results.kv')


class RaceScreenManager(ScreenManager):
    pass


class SlugsStats(BoxLayout):
    name = StringProperty("")
    wins = NumericProperty(0)
    win_percent = NumericProperty(0)


class PlayerStats(BoxLayout):
    name = StringProperty("")
    money = NumericProperty(0)


class SlugsInfo(BoxLayout):
    y_position = NumericProperty(0)
    name = StringProperty("")
    wins = NumericProperty(0)


class RaceScreen(Screen):
    pass