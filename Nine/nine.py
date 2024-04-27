# File name: nine.py - основное окно игры

import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


# базовый класс для динамических объектов игры (игрок, противник, бонус)
class Players:

    names = 'player' # имя игрока, противника, бонуса
    colors = 'black' # цвет игрока, противника, бонуса

    def __init__(self, digit, init_x, init_y):

        self.digit = digit # цифра игрока, противника, бонуса
        self.init_x = init_x # начальная координата x
        self.init_y = init_y # начальная координата x


# создаем класс игрока
class Users(Players):
    names = 'user'
    color = 'white'


# создаем класс противника
class Opponent(Players):
    names = 'Opponent'


# создаем класс бонуса
class Bonus(Players):
    names = 'Bonus'
    colors = 'green'


class NineBoxLayout(BoxLayout):
    user1 = Users(3, 10, 10)
    user1.names = 'new name'

    oppnent1 = Opponent(0, 22, 34)

    bonus1 = Bonus(1, 77, 164)
    bonus1.colors = 'red'

    
    print(user1.__dict__)
    print(oppnent1.__dict__)
    print(bonus1.__dict__)



class NineApp(App):
    def build(self):
        return NineBoxLayout()
    

if __name__ == '__main__':
    NineApp().run()