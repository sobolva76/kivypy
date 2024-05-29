# File name: nine_test5.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


# класс противника в рнем - скорость по осям и функция движения
class Apponent(Widget):
    vel_apponent_x = NumericProperty(0)
    vel_apponent_y = NumericProperty(0)
    vel_apponent = ReferenceListProperty(vel_apponent_x, vel_apponent_y)

    name_apponent = "apponent" # имя противника (по имени будем определять что делать с игроком)

    def move(self):
        """ функция движения противника """
        self.pos = Vector(*self.vel_apponent) + self.pos


# основной класс приложения
class NineTest(Widget):
    #apponent = ObjectProperty(None)# создаем пустой объект противника

    apponent_list = DictProperty({})# список противников (пустой)

    def spawn_apponent(self, *args):
        apponent = ObjectProperty(None)# создаем пустой объект противника

        # создаем противника и добавляем его на экран, и придаем ускоренгие
        apponent = Apponent(pos = (50, 300))
        self.add_widget(apponent)
        apponent.vel_apponent = (0, -2)

        self.apponent_list.update({apponent: apponent.name_apponent})# записываем аппонента в список


    def serve_objects(self):
        """ функция инициализации объектов"""
        #apponent = ObjectProperty(None)# создаем пустой объект противника

        # создаем противника и добавляем его на экран, и придаем ускоренгие
        #apponent = Apponent(pos = (50, 50))
        #self.add_widget(apponent)
        #self.apponent.vel_apponent = vel

        #self.apponent_list.update({apponent: apponent.name_apponent})# записываем аппонента в список

        #spawn_apponent(self)
        #spawns = spawn_apponent(self)
        #Clock.schedule_once(spawns, 2)
        #Clock.schedule_interval(spawns, 1 / 60.0)

        #for i in range(10):
            #Apponent.spawn_apponent(self)
            #spawn_apponent(self)
            #spawns = Apponent.spawn_apponent(self)
            #Clock.schedule_once(Apponent.spawn_apponent, 5)
            #print("Spawn", self.apponent_list)


    def update(self, dt):
        """ функция обновления - основной цикл приложения"""

        for apponents in self.apponent_list.keys():# проходим по списку противников
            #apponents.vel_apponent = (2, 0)
            apponents.move()


# класс запуска приложения
class Nine_test5App(App):
    def build(self):
        game = NineTest()
        #Clock.schedule_once(game.spawn_apponent, 5)# срабатывает один раз с задержкой 5 сек
        Clock.schedule_interval(game.spawn_apponent, 1 / 1)
        game.serve_objects()
        Clock.schedule_interval(game.update, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_test5App().run()