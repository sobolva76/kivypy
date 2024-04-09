# File name: test.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty, NumericProperty


class TestScreen(BoxLayout):

    label = ObjectProperty()
    button1 = ObjectProperty()
    button2 = ObjectProperty()

    counter = NumericProperty(0)

    def set_text(self):
        self.label.text = str(self.counter)
        self.button1.text = str(self.counter * 10)
        self.button2.text = str(self.counter * 100)

        self.counter +=1


class TestApp(App):
    def build(self):
        return TestScreen()
    

if __name__ == '__main__':
    TestApp().run()