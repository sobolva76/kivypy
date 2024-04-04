# File name: test.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TestScreen(BoxLayout):
    pass


class TestApp(App):
    def build(self):
        return TestScreen()
    

if __name__ == '__main__':
    TestApp().run()