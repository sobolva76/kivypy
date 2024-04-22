# File name: ninereg - работает при первой загрузке игры, регистрация пользователя

import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class Basebox(BoxLayout):
    pass


class NineregApp(App):
    def build(self):
        return Basebox()
    

if __name__ == '__main__':
    NineregApp().run()