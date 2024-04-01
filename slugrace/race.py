# File name: race.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class RaceApp(App):
    def build(self):
        return BoxLayout()


if __name__ == '__main__':
    RaceApp().run()