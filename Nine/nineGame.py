# File name: nine_test5.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button


class Move_button(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("касание Test_button", touch)


class Blok(Widget):
    """ Класс блоков """ 
    pass


class Blok_stop(Widget):
    """ Класс блоков определяющих конец планки и конечного блока(при столкновении с ним - удаляется аппонент)"""
    pass


class Blok_base(Widget):
    """ класс блоков расположенных на уровне (не включая пол и стены) """
    blok_base_name = "blok_base"


class Blok_end(Widget):
    """ блок указывающий окончание горизонта 
    (определяет когда включать скорость по оси Y и делать скорость по оси X = 0 )"""
    blok_end_name = "blok_end"


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
    
    # горизонтальные блоки с блоком окончания
    blok_base = ObjectProperty(None)
    blok_end = ObjectProperty(None)

    apponent_list = DictProperty({})# список противников (пустой)
    blok_list = DictProperty({})# список блоков
    collision_list = DictProperty({})# список заполняется при первой коллизии аппонента с блоком

    spawn_l_r = True# переменная определяющая где спавнить аппонента, с лева=True, с права=False


    def on_touch_down(self, touch):
        if self.btn_right.collide_point(*touch.pos):
            self.player.vel_player = (2, 0)
            print("касание player движется", touch)

        if self.btn_left.collide_point(*touch.pos):
            self.player.vel_player = (-2, 0)
            print("касание player движется", touch)

        if self.btn_up.collide_point(*touch.pos):
            self.player.vel_player_y = 28
            print("касание player движется", touch)

    def on_touch_up(self, touch):
        #return super().on_touch_up(touch)
        if self.btn_right.collide_point(*touch.pos):
            self.player.vel_player = (0, 0)
            print("убираем player стоп", touch)

        if self.btn_left.collide_point(*touch.pos):
            self.player.vel_player = (0, 0)
            print("убираем player стоп", touch)

        if self.btn_up.collide_point(*touch.pos):
            self.player.vel_player = (0, 0)
            print("убираем player стоп", touch)

    
    def spawn_apponent(self, *args):
        """ функция спавна противников - создает и записывает в спивок"""
        # определяем колличество аппонентов на уровне
        if len(self.apponent_list) < 1:
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

        self.player.vel_player = vel
        print(self.player.vel_player)

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
        blok_end = Blok_end(size = (10, 10), pos = (525, 165))
        self.blok_list.update({blok_end: blok_end.blok_end_name})
        self.add_widget(blok_end)

        blok_base = Blok_base(size = (700, 10), pos = (200, 220))
        self.blok_list.update({blok_base: blok_base.blok_base_name})
        self.add_widget(blok_base)
        blok_end = Blok_end(size = (10, 10), pos = (175, 235))
        self.blok_list.update({blok_end: blok_end.blok_end_name})
        self.add_widget(blok_end)

        blok_base = Blok_base(size = (300, 10), pos = (10, 300))
        self.blok_list.update({blok_base: blok_base.blok_base_name})
        self.add_widget(blok_base)
        blok_end = Blok_end(size = (10, 10), pos = (325, 310))
        self.blok_list.update({blok_end: blok_end.blok_end_name})
        self.add_widget(blok_end)

        #print(self.blok_list)

    def move_player(self, dt):

        self.player.move_player()

        if self.player.vel_player_y != 0:

            for blok_l in self.blok_list.keys():
            
                if self.player.collide_widget(blok_l):
                    
                    self.collision_list[self.player] = blok_l
                    self.player.vel_player_y = 0

        elif self.collision_list.get(self.player):
        #self.collision_list.get(self.player)
            if self.player.collide_widget(self.collision_list[self.player]): 
                print(self.collision_list[self.player])
            else:
                self.collision_list.pop(self.player)
                self.player.vel_player = (0, -2)
                print(self.collision_list)

        else:
            self.player.vel_player_y = -2

        
        

# ********************************************
# далее (между ***) идет попытка определения коллизий по углам прямоугольника
        # левый нижний угол
        player_x = self.player.pos[0]
        player_y = self.player.pos[1]

        #левый верхний угол
        player_top_left_x = self.player.pos[0]
        player_top_left_y = self.player.pos[1] + self.player.size[1]

        # правый верхний угол
        player_top_right_x = self.player.pos[0] + self.player.size[0]
        player_top_right_y = self.player.pos[1] + self.player.size[1]

        # нижний правый угол
        player_buttom_right_x = self.player.pos[0] + self.player.size[0]
        player_buttom_right_y = self.player.pos[1]

        #print(player_x, "*", player_y, "/", player_top_left_x, "*", player_top_left_y, "/", player_top_right_x, "*", player_top_right_y, "/", player_buttom_right_x, "*", player_buttom_right_y)

        #for blok_l in self.blok_list.keys():
            #x_blok, y_blok = blok_l.pos
            #blok_width, blok_height = blok_l.size

            #print(x_blok, player_y, "*", y_blok, player_y)

            #if x_blok > player_x and y_blok > player_y and x_blok + blok_width > player_buttom_right_x:
                #self.player.vel_player_y = 0
                #print("collide", x_blok, player_x, "*", y_blok, player_y)
                #return
            #else:
                #self.player.vel_player_y = -2
                #print("not-collide")
# ******************************************************


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
                        # ПОКА - направление движения не меняется у аппонента
                        # если он начал с лева то и движется всегда в лево(при смене горизонтальных блоков)
                        # возможно потом необходимо это изменить на - если он изменид направление после
                        # удара о стенку, то должен и дальше двигаться в новом направлении
                        apponents.vel_apponent_x *= -1

                    
                    # проверка на столкновение с горизонтальной(или) балкой
                    if self.blok_list.get(bloks) == 'blok_base' and self.collision_list.get(apponents) != bloks:

                        # если небыло коллизий - записываем в список и меняем скорость
                        # но перед этим проверяем какая префикс l=+x, r=-x
                        if (apponents.name_apponent == "apponent_l"):
                            apponents.vel_apponent = (2, 0)
                        elif (apponents.name_apponent == "apponent_r"):
                            apponents.vel_apponent = (-2, 0)
                        self.collision_list[apponents] = bloks

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
                        if (apponents.name_apponent == "apponent_r"):
                            apponents.vel_apponent = (-2, 0)
                        else:
                            apponents.vel_apponent = (2, 0)

                        self.collision_list[apponents] = bloks

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
        Clock.schedule_interval(game.move_player, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    NineGame().run()