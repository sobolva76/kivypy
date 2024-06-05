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


class Blok_stop(Widget):
    """ Класс блоков определяющих конец планки и конечного блока(при столкновении с ним - удаляется аппонент)"""
    pass


class Blok_base(Widget):
    """ клпсс блоков расположенных на уровне (не включая пол и стены) """
    blok_base_name = "blok_base"


class Blok_end(Widget):
    """ блок указывающий окончание горизонта 
    (определяет когда включать скорость по оси Y и делать скорость по оси X = 0 )"""
    blok_end_name = "blok_end"


# класс противника в нем - скорость по осям, функция движения и имя
class Apponent(Widget):
    """ сласс противникоа имеет скорость движения по осям, имя и функцию движения"""
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
    blok_stop = ObjectProperty(None)
    blok_stop_name = "blok_stop"

    blok_base = ObjectProperty(None)
    blok_end = ObjectProperty(None)

    apponent_list = DictProperty({})# список противников (пустой)
    blok_list = DictProperty({})# список блоков
    collision_list = DictProperty({})# список заполняется при первой коллизии аппонента с блоком

    
    def spawn_apponent(self, *args):
        """ функция спавна противников - создает и записывает в спивок"""
        # определяем колличество аппонентов на уровне
        if len(self.apponent_list) < 4:
            apponent = ObjectProperty(None)# создаем пустой объект противника

            # создаем противника и добавляем его на экран, и придаем ускорение
            if ((len(self.apponent_list))/2):
                apponent = Apponent(pos = (100, 500))
            else:
                apponent = Apponent(pos = (500, 500))
            self.add_widget(apponent)
            apponent.vel_apponent = (0, -2)
            self.apponent_list.update({apponent: apponent.name_apponent})# записываем аппонента в список


    def serve_objects(self):
        """ функция инициализации объектов"""

        # инициализация блоков
        # инициализируем пол и стены
        self.blok_list.update({self.blok_right: self.blok_right_name})
        self.blok_list.update({self.blok_left: self.blok_left_name})
        self.blok_list.update({self.blok_down: self.blok_down_name})
        self.blok_list.update({self.blok_stop: self.blok_stop_name})

        blok_base = Blok_base(size = (500, 10), pos = (10, 150))
        self.blok_list.update({blok_base: blok_base.blok_base_name})
        self.add_widget(blok_base)
        blok_end = Blok_end(size = (10, 10), pos = (525, 165))
        self.blok_list.update({blok_end: blok_end.blok_end_name})
        self.add_widget(blok_end)

        blok_base = Blok_base(size = (300, 10), pos = (10, 300))
        self.blok_list.update({blok_base: blok_base.blok_base_name})
        self.add_widget(blok_base)
        blok_end = Blok_end(size = (10, 10), pos = (325, 310))
        self.blok_list.update({blok_end: blok_end.blok_end_name})
        self.add_widget(blok_end)

        #print(self.blok_list)


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
                        # меняем скорость на противоположную
                        apponents.vel_apponent_x *= -1
                    
                    # проверка на столкновение с горизонтальной(или) балкой
                    if self.blok_list.get(bloks) == 'blok_base' and self.collision_list.get(apponents) != bloks:
                        # если небыло коллизий - записываем в список и меняем скорость
                        self.collision_list[apponents] = bloks
                        apponents.vel_apponent = (2, 0)

                    # блок окончания горизонта - коллизии происходят каждые несколько кадров
                    # и из-за этого появились проблемы(когда нет коллизии аппонент должен изменить скорость
                    # по x=0 по y=-2, тоесть падать, но планка еще не закончилась),
                    # что-бы решить их был введен список коллизий
                    # куда записывалась первая коллизия, а блок blok_end определяет 
                    # где кончается горизонтальная планка и меняет скорость на x=0, y=-2
                    if self.blok_list.get(bloks) == 'blok_end':
                        # если небыло коллизий - записываем в список и меняем скорость
                        if self.collision_list.get(apponents):
                            self.collision_list.pop(apponents)
                            apponents.vel_apponent = (0, -2)

                    # проверяем на столкновение с полом и записываем в список коллизий
                    # что-бы исключить повторные столкновения
                    if self.blok_list.get(bloks) == 'blok_down' and self.collision_list.get(apponents) != bloks:
                        # если небыло коллизий - записываем в список и меняем скорость
                        self.collision_list[apponents] = bloks
                        apponents.vel_apponent = (2, 0)

                    # проверяем на столкновение аппонента с конечным блоком
                    # (блок конца его пути, после виджет(аппонента) удаляем)
                    if self.blok_list.get(bloks) == 'blok_stop' and self.apponent_list.get(apponents):
                        # записываем в список коллизий
                        self.collision_list[apponents] = bloks
                        
        # создаем копию списка коллизий, проверяем кто из аппонентов столкнулся с конечным блоком
        # и затем удаляем этого аппанента из всех списков, 
        # затем удаляем и его 
        cort_copy = self.collision_list.copy()
        collide_corte = cort_copy.items()
        for corts in collide_corte:
            if corts[1] == self.blok_stop:
                self.collision_list.pop(corts[0])
                self.apponent_list.pop(corts[0])
                self.remove_widget(corts[0])
        


# класс запуска приложения
class NineGame(App):
    def build(self):
        game = NineGameBase()
        # спавн аппонентов, сколько аппонентов в секунду (сейчас один раз в 3 секунды)
        Clock.schedule_interval(game.spawn_apponent, 3 / 1) # в н сикунд / н раз
        # инициализация объектов
        game.serve_objects()
        # запуск основного цикла - обновляется каждую секунду
        Clock.schedule_interval(game.update, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    NineGame().run()