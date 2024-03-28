from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup


class WidgetStartPopup(Widget):
    def startpopup(self):
        show_popup()


class MyPopup(FloatLayout):
    pass


def show_popup():
    show = MyPopup()

    popupWindow = Popup(title = "Всплывающее окно", content = show,
                         size_hint = (None, None), size = (200, 200))
    
    popupWindow.open()


class K_popupApp(App):
    def build(self):
        return WidgetStartPopup()
    

if __name__ == '__main__':
    myApp = K_popupApp()
    myApp.run()