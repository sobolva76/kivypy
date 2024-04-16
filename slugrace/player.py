# File name: player.py

from kivy.properties import StringProperty, NumericProperty
from kivy.event import EventDispatcher


class Player(EventDispatcher):
    name = StringProperty('')
    initial_money = NumericProperty(0) # начальная сумма
    money = NumericProperty(0) # наличие денег в определенный момент
    money_before_race = NumericProperty(0) # наличие до начала гонки
    money_won = NumericProperty(0) # колличество выигранных денег(- если проиграл)
    bet = NumericProperty(0) # сумма ставки игрока