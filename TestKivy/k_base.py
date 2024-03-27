from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class MyGridLayout(GridLayout):
    pass


class MyBoxLayout(BoxLayout):
    pass


class MyWidget(Widget):
    pass


class K_baseApp(App):
    def build(self):
        return MyGridLayout()
    

if __name__ == '__main__':
    myApp = K_baseApp()
    myApp.run()