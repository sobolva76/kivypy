# File name: nine_test5.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


# класс противника в нем - скорость по осям, функция движения и имя
class Apponent(Widget):
    vel_apponent_x = NumericProperty(0)
    vel_apponent_y = NumericProperty(0)
    vel_apponent = ReferenceListProperty(vel_apponent_x, vel_apponent_y)

    name_apponent = "apponent" # имя противника (по имени будем определять что делать с игроком)

    def move(self):
        """ функция движения противника """
        self.pos = Vector(*self.vel_apponent) + self.pos


# основной класс приложения
class NineGameBase(Widget):

    apponent_list = DictProperty({})# список противников (пустой)

    def spawn_apponent(self, *args):
        """ функция спавна противников - создает и записывает в спивок"""
        apponent = ObjectProperty(None)# создаем пустой объект противника

        # создаем противника и добавляем его на экран, и придаем ускорение
        apponent = Apponent(pos = (50, 300))
        self.add_widget(apponent)
        apponent.vel_apponent = (0, -2)

        self.apponent_list.update({apponent: apponent.name_apponent})# записываем аппонента в список


    def serve_objects(self):
        """ функция инициализации объектов"""


    def update(self, dt):
        """ функция обновления - основной цикл приложения"""

        for apponents in self.apponent_list.keys():# проходим по списку противников
            # запускаем функцию движения для каждого противника
            apponents.move()


# класс запуска приложения
class NineGame(App):
    def build(self):
        game = NineGameBase()
        Clock.schedule_interval(game.spawn_apponent, 1 / 2) # 2 раза в секунду
        game.serve_objects()
        Clock.schedule_interval(game.update, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    NineGame().run()