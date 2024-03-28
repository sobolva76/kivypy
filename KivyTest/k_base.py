from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch


class MySpiner(FloatLayout):
    def spiner_clicked(self, value):
        print("Выбрано - " + value)


class MySwitch(GridLayout):
    def switch_callback(self, switchObject, switchValue):
        if (switchValue):
            print("Переключатель включен")
        else:
            print("Переключатель выключен")


class CheckBoxLayout(BoxLayout):
    def checkbox_click(self, instance, value):
        if value is True:
            print("Чекбокс астивен")
        else:
            print("Чекбокс не активет")


class MyTextInput(Widget):
    #через app - работает а здесь нет !!!!!!!!!
    # плюс - не меняется размер на ширину грида!!!!!!!
    #def process(self):
     #   text = self.TextInput.ids.input.text
      #  print(text)
    pass


class MyBoxLayout(BoxLayout):
    def printMe(self_xx, yy):
        print(yy)


class CanvasWidget(Widget):
    pass


class MyGridLayout(GridLayout):
    pass


class K_baseApp(App):
    def build(self):
        myLayout = MyGridLayout()
        return myLayout
    
    def process(self):
        text = self.root.ids.input.text
        print(text)
        


if __name__=="__main__":
    myapp = K_baseApp()
    myapp.run()
