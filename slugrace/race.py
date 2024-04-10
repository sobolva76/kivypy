# File name: race.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty, StringProperty

from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')


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


class SlugImage(RelativeLayout):
    body_image = StringProperty('')
    eye_image = StringProperty('')
    y_position = NumericProperty(0)


class RaceScreen(BoxLayout):
    pass

class RaceApp(App):
    def build(self):
        return RaceScreen()


if __name__ == '__main__':
    RaceApp().run()