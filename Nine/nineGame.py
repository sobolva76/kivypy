# File name: nine_test5.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Blok(Widget):
    """ Класс блоков """
    pass


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

    # создание постоянных неизменяемых блоков
    blok_right = ObjectProperty(None)
    blok_right_name = "blok_right"
    blok_left = ObjectProperty(None)
    blok_left_name = "blok_left"
    blok_down = ObjectProperty(None)
    blok_down_name = "blok_down"

    apponent_list = DictProperty({})# список противников (пустой)
    blok_list = DictProperty({})# список блоков

    def spawn_apponent(self, *args):
        """ функция спавна противников - создает и записывает в спивок"""
        apponent = ObjectProperty(None)# создаем пустой объект противника

        # создаем противника и добавляем его на экран, и придаем ускорение
        apponent = Apponent(pos = (50, 300))
        self.add_widget(apponent)
        apponent.vel_apponent = (2, 0)

        self.apponent_list.update({apponent: apponent.name_apponent})# записываем аппонента в список


    def serve_objects(self):
        """ функция инициализации объектов"""

        # инициализация блоков
        self.blok_list.update({self.blok_right: self.blok_right_name})
        self.blok_list.update({self.blok_left: self.blok_left_name})
        self.blok_list.update({self.blok_down: self.blok_down_name})

        print(self.blok_list)


    def update(self, dt):
        """ функция обновления - основной цикл приложения"""

        for apponents in self.apponent_list.keys():# проходим по списку противников
            # запускаем функцию движения для каждого противника
            apponents.move()

            for bloks in self.blok_list.keys():# проходим по списку блоков
                # проверяем столкновения с блоками
                if apponents.collide_widget(bloks):
                    # проверка на столкновение со стенами
                    if self.blok_list.get(bloks) == 'blok_right' or self.blok_list.get(bloks) == 'blok_left':
                        #apponents.velocity_x *= -1
                        print(apponents)

                    if self.blok_list.get(bloks) == 'blok_down':
                        apponents.velocity_x = 2
                        print("collide down")


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