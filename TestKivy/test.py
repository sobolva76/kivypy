from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MyWidget(Widget):
    Label.text = "Ass"


class MlabelApp(App):
    def build(self):
        return MyWidget()
    

if __name__ == '__main__':
    MlabelApp().run()