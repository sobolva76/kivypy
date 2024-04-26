# File name: nine.py - основное окно игры

import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class NineBoxLayout(BoxLayout):
    pass


class NineApp(App):
    def build(self):
        return NineBoxLayout()
    

if __name__ == '__main__':
    NineApp().run()