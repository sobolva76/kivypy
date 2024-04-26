# File name: ninebase.py - окно при загрузке(после регистрации), переходах между уровнями и этажами, при паузе

import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class BaseBoxLayout(BoxLayout):
    pass


class NinebaseApp(App):
    def build(self):
        return BaseBoxLayout()
    

if __name__ == '__main__':
    NinebaseApp().run()