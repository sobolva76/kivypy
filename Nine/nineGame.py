# File name: nine_test5.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.window import Window


class Move_button(Button):
    """ класс кнопок движения персонажа по x, и прыжок(y)"""
    pass
    #def on_touch_down(self, touch):
        #if self.collide_point(*touch.pos):
            #print("касание Test_button", touch)


class Blok(Widget):
    """ Класс постоянных блоков блоков - стены, пол, потолок, и нижняя кайма """ 
    pass


class Blok_stop(Widget):
    """ Класс конечного блока(при столкновении с ним - удаляется аппонент)"""
    pass


class Blok_base(Widget):
    """ класс блоков расположенных на уровне (не включая пол и стены) """
    blok_base_name = "blok_base"


# класс противника в нем - скорость по осям, функция движения и имя
class Apponent(Widget):
    """ класс противникоа имеет скорость движения по осям, имя и функцию движения"""
    vel_apponent_x = NumericProperty(0)
    vel_apponent_y = NumericProperty(0)
    vel_apponent = ReferenceListProperty(vel_apponent_x, vel_apponent_y)

    name_apponent = "apponent" # имя противника (по имени будем определять что делать с игроком)

    def move(self):
        """ функция движения противника """
        self.pos = Vector(*self.vel_apponent) + self.pos


class Player(Widget):
    """ класс персонажа имеет скорость движения по осям, имя и функцию движения """

    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)

    vel_player_x = NumericProperty(0)
    vel_player_y = NumericProperty(0)
    vel_player = ReferenceListProperty(vel_player_x, vel_player_y)

    name_apponent = "apponent" # имя противника (по имени будем определять что делать с игроком)

    def move_player(self):
        """ функция движения противника """
        self.pos = Vector(*self.vel_player) + self.pos


# основной класс приложения
class NineGameBase(Widget):

    def __init__(self, **kwargs):
        super(NineGameBase, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)


    def _keydown(self,*args):
        if args[3] == "a":
            self.player.vel_player_x = -2
            print(args[3], "++")
        if args[3] == "d":
            self.player.vel_player_x = 2
            print(args[3], "++")
        if args[3] == " ":
            self.player.vel_player_y = 10
            print(args[3], "++")


    def _keyup(self,*args):

        if args[1] == 97 or args[1] == 100:
            self.player.vel_player_x = 0
        if args[1] == 32:
            self.player.vel_player_y = 0
        print(args[1], " -- ")

    # инициализация игрока и кнопок
    player = ObjectProperty(None)
    btn_right = ObjectProperty(None)
    btn_left = ObjectProperty(None)
    btn_up = ObjectProperty(None)

    # создание постоянных неизменяемых блоков
    blok_right = ObjectProperty(None)
    blok_right_name = "blok_right"
    blok_left = ObjectProperty(None)
    blok_left_name = "blok_left"
    blok_down = ObjectProperty(None)
    blok_down_name = "blok_down"
    blok_stop = ObjectProperty(None)
    blok_stop_name = "blok_stop"
    
    # горизонтальные блоки
    blok_base = ObjectProperty(None)

    apponent_list = DictProperty({})# список противников (пустой)
    blok_list = DictProperty({})# список блоков
    collision_list = DictProperty({})# список заполняется при первой коллизии аппонента с блоком

    spawn_l_r = True# переменная определяющая где спавнить аппонента, с лева=True, с права=False


    def on_touch_down(self, touch):
        if self.btn_right.collide_point(*touch.pos):
            if self.player.collide_widget(self.blok_right):
                 self.player.vel_player_x = 0
            else:
                self.player.vel_player_x = 2

        if self.btn_left.collide_point(*touch.pos):
            if self.player.collide_widget(self.blok_left):
                 self.player.vel_player_x = 0
                 print("удар о стену")
            else:
                self.player.vel_player_x = -2

        if self.btn_up.collide_point(*touch.pos):
            #if self.collision_list.get(self.player):
                #self.collision_list.pop(self.player)
            self.player.vel_player_y = 10

    def on_touch_up(self, touch):
        
        if self.btn_right.collide_point(*touch.pos):
            self.player.vel_player = (0, 0)

        if self.btn_left.collide_point(*touch.pos):
            self.player.vel_player = (0, 0)

        if self.btn_up.collide_point(*touch.pos):
            if self.collision_list.get(self.player):
                self.collision_list.pop(self.player)
            self.player.vel_player_y = -2
            print("отпустил прыжок", self.collision_list)

    
    def spawn_apponent(self, *args):
        """ функция спавна противников - создает и записывает в спивок"""
        # определяем колличество аппонентов на уровне
        if len(self.apponent_list) < 10:
            apponent = ObjectProperty(None)# создаем пустой объект противника

            # создаем противника и добавляем его на экран, и придаем ускорение
            # плюс - проверяем где его спавнить
            if (self.spawn_l_r):
                apponent = Apponent(pos = (100, 500))
                self.spawn_l_r = False
                apponent.name_apponent = "apponent_l"
            else:
                apponent = Apponent(pos = (500, 500))
                self.spawn_l_r = True
                apponent.name_apponent = "apponent_r"

            self.add_widget(apponent)
            apponent.vel_apponent = (0, -2)
            self.apponent_list.update({apponent: apponent.name_apponent})# записываем аппонента в список


    def serve_objects(self, vel=(0, -2)):
        """ функция инициализации объектов"""

        # определение скорости персонажа
        self.player.vel_player = vel

        # инициализация блоков
        # инициализируем пол и стены
        self.blok_list.update({self.blok_right: self.blok_right_name})
        self.blok_list.update({self.blok_left: self.blok_left_name})
        self.blok_list.update({self.blok_down: self.blok_down_name})
        self.blok_list.update({self.blok_stop: self.blok_stop_name})

        # инициализация горизонтальных блоков
        blok_base = Blok_base(size = (500, 10), pos = (10, 150))
        self.blok_list.update({blok_base: blok_base.blok_base_name})
        self.add_widget(blok_base)

        blok_base = Blok_base(size = (700, 10), pos = (200, 220))
        self.blok_list.update({blok_base: blok_base.blok_base_name})
        self.add_widget(blok_base)

        blok_base = Blok_base(size = (300, 10), pos = (10, 300))
        self.blok_list.update({blok_base: blok_base.blok_base_name})
        self.add_widget(blok_base)

    def mov_player(self, dt):
        """ функция движения персонажа, при падении проверяем столкновение в цикле"""

        # движение персонажа
        self.player.move_player()
        # если падаем то проверяем в цикле коллизии с блоками
        if self.player.vel_player_y != 0:

            for blok_l in self.blok_list.keys():
            
                if self.player.collide_widget(blok_l):
                    # если есть коллизия - записываем в ссписок коллизий и делаем скорость по y=0
                    self.collision_list[self.player] = blok_l
                    self.player.vel_player_y = 0
        
        # проверяем запись в списке коллизий - если есть то проверяем на столкновение только этот блок
        elif self.collision_list.get(self.player):
        
            if self.player.collide_widget(self.collision_list[self.player]): 
                pass

            # если коллизий больше нет - очищаем список коллизий и делаем скорость по x=0, y=-2
            else:
                self.collision_list.pop(self.player)
                self.player.vel_player = (0, -2)

        else:
            self.player.vel_player_y = -2

        # проверка на столкновение со стенами
        # ПРОБЛЕМА - если стоит у стены то при прыжке не падает вниз
        # - пока решил ее добовлением 5 пикселей при столкновении о стену
        if self.player.collide_widget(self.blok_left):
            self.player.pos[0] = self.player.pos[0] + 5 
        elif self.player.collide_widget(self.blok_right):
            self.player.pos[0] = self.player.pos[0] - 5


    def update(self, dt):
        """ функция обновления - основной цикл приложения"""

        for apponents in self.apponent_list.keys():# проходим по списку противников
            # запускаем функцию движения для каждого противника
            apponents.move()
            # если скорость по y=-2(то мы падаем)
            if  apponents.vel_apponent_y != 0:

                for bloks in self.blok_list.keys():# проходим по списку блоков
                    # проверяем столкновения с блоками
                    if apponents.collide_widget(bloks):

                        # проверка на столкновение с горизонтальной балкой
                        # и проверяем записано ли столкновение в список
                        if self.blok_list.get(bloks) == 'blok_base' and self.collision_list.get(apponents) != bloks:

                            # если небыло коллизий - записываем в список и меняем скорость
                            # но перед этим проверяем какая префикс l=+x, r=-x
                            if (self.apponent_list[apponents] == "apponent_l"):
                                apponents.vel_apponent = (2, 0)
                            else:
                                apponents.vel_apponent = (-2, 0)
                            self.collision_list[apponents] = bloks

                        # проверяем на столкновение с полом и записываем в список коллизий
                        # что-бы исключить повторные столкновения
                        if self.blok_list.get(bloks) == 'blok_down' and self.collision_list.get(apponents) != bloks:
                            # если небыло коллизий - записываем в список и меняем скорость
                            if (self.apponent_list[apponents] == "apponent_l"):
                                apponents.vel_apponent = (2, 0)
                            else:
                                apponents.vel_apponent = (-2, 0)
                            self.collision_list[apponents] = bloks

            # проверяем на столкновение аппонента с конечным блоком
            # (блок конца его пути, после виджет(аппонента) удаляем)
            elif apponents.collide_widget(self.blok_stop) and self.apponent_list.get(apponents):
                # записываем в список коллизий
                self.collision_list[apponents] = self.blok_stop

            # проверка на столкновение со стенами
            elif apponents.collide_widget(self.blok_right) or apponents.collide_widget(self.blok_left):
                # меняем скорость на противоположную при столкновении с стеной - и меняем префикс
                apponents.vel_apponent_x *= -1
                if (self.apponent_list[apponents] == "apponent_r"):
                    self.apponent_list[apponents] = "apponent_l" 
                else:
                    self.apponent_list[apponents] = "apponent_r"

            # проверяем на столкновение с блоком внесенным в список аоллизий
            elif self.collision_list.get(apponents):
                if apponents.collide_widget(self.collision_list[apponents]): 
                    pass

                # если коллизий больше нет - очищаем список коллизий и делаем скорость по x=0, y=-2
                else:
                    self.collision_list.pop(apponents)
                    apponents.vel_apponent = (0, -2)
                        
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
        Clock.schedule_interval(game.mov_player, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    NineGame().run()