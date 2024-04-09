# File name: results.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')

class ResultsScreen(BoxLayout):
    pass

class ResultsApp(App):
    def build(self):
        return ResultsScreen()

if __name__ == '__main__':
    ResultsApp().run()