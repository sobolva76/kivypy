# необходимые модули
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image

# подключение этажей
# делать - или сюда подключать сотню файлов(можно через for)
# - или - делать уровни рандомно 
# лучше - делать шаблон а в него считывать из файла данные
import_test = "levels_1"
import nineLevels.lev_1.levels_1 as levels

class AnimatingImage(Image):

    def __init__(self, **kwargs):
        super(AnimatingImage, self).__init__(**kwargs)

        self.source = "atlas://invader/frame1"
    #test_textures = "atlas://invader/frame1"
    #print(textures.test_textures)
    #pass
   


class Player(Widget):
    """ класс персонажа имеет скорость движения по осям, имя и функцию движения """

    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)

    vel_player_x = NumericProperty(0)
    vel_player_y = NumericProperty(0)
    vel_player = ReferenceListProperty(vel_player_x, vel_player_y)

    name_apponent = "apponent" # имя противника (по имени будем определять что делать с игроком)
    coll_life = 9# колличество жизни (при первом варианте колличество попыток на этаж)

    def move_player(self):
        """ функция движения противника """
        self.pos = Vector(*self.vel_player) + self.pos


class Apponent(Widget):
    """ класс противникоа имеет скорость движения по осям, имя и функцию движения"""
    vel_apponent_x = NumericProperty(0)
    vel_apponent_y = NumericProperty(0)
    vel_apponent = ReferenceListProperty(vel_apponent_x, vel_apponent_y)

    name_apponent = "apponent" # имя противника (по имени будем определять что делать с игроком)

    def move(self):
        """ функция движения противника """
        self.pos = Vector(*self.vel_apponent) + self.pos


class Move_button(Button):
    """ класс кнопок движения персонажа по x, и прыжок(y)"""
    pass


class Blok(Widget):
    """ Класс постоянных блоков блоков - стены, пол, потолок """ 
    pass


class Blok_stop(Widget):
    """ Класс конечного блока(при столкновении с ним - удаляется аппонент)"""
    pass


class Blok_end(Widget):
    """ Класс перехода между этажами """
    blok_end_name = "blok_end"


class Blok_base(Widget):
    """ класс блоков расположенных на уровне (не включая пол и стены) """
    blok_base_name = "blok_base"


class GameStartScreen(Screen):
    """ Главный класс игры """

    #invader = ObjectProperty(None)

    # переменная в которую записываем текущую коллизию (последний блок на котором был персонаж)
    # она нужна при проверки на удержание клавиши прыжка
    vr = None
    # переменная ограничивающая колличество прыжков
    # False - прыгать нельзя - меняется при коллизии с нижним блоком
    bjump = False

    # инициализация игрока 
    player = ObjectProperty(None)

    # создание постоянных неизменяемых блоков
    blok_right = ObjectProperty(None)# стена
    blok_right_name = "blok_right"
    blok_left = ObjectProperty(None)# стена
    blok_left_name = "blok_left"
    blok_down = ObjectProperty(None)# пол (последний горизонтальный блок)
    blok_down_name = "blok_down"

    # блок уничтожения аппонентов, устанавливается слево на полу
    blok_stop = ObjectProperty(None)
    blok_stop_name = "blok_stop"

    # список блоков учавствующих в столкновениях
    blok_list = DictProperty({})

    # ниже переменные противника
    apponent = ObjectProperty(None)# создаем пустой объект противника
    apponent_list = DictProperty({})# список противников (пустой)
    spawn_l_r = True# переменная определяющая где спавнить аппонента, с лева=True, с права=False

    # список заполняется при первой коллизии аппонента с блоком
    collision_list = DictProperty({})

    # горизонтальные блоки
    blok_base = ObjectProperty(None)

    # блок перехода между этажами
    blok_end = ObjectProperty(None)

    # далее кнопки
    btn_right = ObjectProperty(None)# движение вправо
    btn_left = ObjectProperty(None)# движение влево
    btn_up = ObjectProperty(None)# прыжок

    # далее кнопки перехода на другие скрины
    # при переходе игра становится на паузу (Clock - останавливается)
    btn_screen_end = ObjectProperty(None)

    # ниже управление с клавиатурой - необходимо только для версии на ПК
#**************************************************************************
    def __init__(self, **kwargs):
        super(GameStartScreen, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)


    def _keydown(self,*args):
        if args[3] == "a":
            self.player.vel_player_x = -2
        if args[3] == "d":
            self.player.vel_player_x = 2
        if args[3] == " ":
            self.player.vel_player_y = 10
            self.bjump = False


    def _keyup(self,*args):

        if args[1] == 97 or args[1] == 100:
            self.player.vel_player_x = 0
        if args[1] == 32:
            self.player.vel_player_y = -2
#**************************************************************************

    # Ниже функции касания экрана - только для телефонов или экранов с этой возможностью
    # заметил - что при использовании touch - кнопки on_press - не работают
    def on_touch_down(self, touch):
        """ функция косания(нажатия)"""
        # движение направо
        if self.btn_right.collide_point(*touch.pos):
            self.player.vel_player_x = 2
        # движение на лево
        if self.btn_left.collide_point(*touch.pos):
            self.player.vel_player_x = -2
        # прыжок - высота 10, 
        # проверяем можно-ли прыгать self.bjump, и не летим ли
        if self.btn_up.collide_point(*touch.pos):
            if self.player.vel_player_y == 0 and self.bjump:
                self.bjump = False 
                self.player.vel_player_y = 10
        # далее дополнительные кнопки
        if self.btn_screen_end.collide_point(*touch.pos):
            self.manager.current = 'screen_gameend'

    def on_touch_up(self, touch):
        """ функция - нет касания"""
        # при отпускании клавиши скорость x=0
        if self.btn_right.collide_point(*touch.pos):
            self.player.vel_player_x = 0
        # при отпускании клавиши скорость x=0
        if self.btn_left.collide_point(*touch.pos):
            self.player.vel_player_x = 0
        # скорость по y после прыжка
        if self.btn_up.collide_point(*touch.pos):
            self.player.vel_player_y = -2    


    def spawn_apponent(self, *args):
        """ функция спавна противников - создает и записывает в спивок"""
        # определяем колличество аппонентов на уровне
        # получаем данные из файла уровней
        if len(self.apponent_list) < levels.get_koll_spawn(self):
            
            # смотрим сколько точек спавна
            if levels.get_koll_point_spawn(self) == 1:
                apponent = Apponent(pos = levels.get_spawn_apponent_r(self))
                self.spawn_l_r = True
                apponent.name_apponent = "apponent_r"
            else:
                # создаем противника и добавляем его на экран, и придаем ускорение
                # плюс - проверяем где его спавнить
                if (self.spawn_l_r):
                    apponent = Apponent(pos = levels.get_spawn_apponent_l(self))
                    self.spawn_l_r = False
                    apponent.name_apponent = "apponent_l"
                else:
                    apponent = Apponent(pos = levels.get_spawn_apponent_r(self))
                    self.spawn_l_r = True
                    apponent.name_apponent = "apponent_r"
            
            # создаем аппонента, даем скорость и записываем в список аппанантов
            self.add_widget(apponent)
            apponent.vel_apponent = (0, -2)
            self.apponent_list.update({apponent: apponent.name_apponent})# записываем аппонента в список

    def move_apponent(self, dt):
        """ функция движения и проверка коллизий аппонента с блоками """

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
            if corts[1] == self.blok_stop and corts[0] != self.player:
                self.collision_list.pop(corts[0])
                self.apponent_list.pop(corts[0])
                self.remove_widget(corts[0])


    def mov_player(self, dt):
        """ функция движения персонажа, при падении проверяем столкновение в цикле"""

        # движение персонажа
        self.player.move_player()
        # если падаем то проверяем в цикле коллизии с блоками
        if self.player.vel_player_y != 0:

            for blok_l in self.blok_list.keys():
            
                if self.player.collide_widget(blok_l):

                    if self.blok_list.get(blok_l) == "blok_end":
                       
                        self.manager.current = 'screen_gameend'
                    
                    # попытка проверить коллизия была сверху или снизу
                    # если коллизия была снизу то сразу y=-2
                    if blok_l.pos[1] > self.player.pos[1]:
                        self.player.vel_player_y = -2
                        self.bjump = False
                
                    else:
                        # если есть коллизия - записываем в ссписок коллизий и делаем скорость по y=0
                        self.collision_list[self.player] = blok_l
                        self.player.vel_player_y = 0
                        self.bjump = True
                        # записываем текущий блок во временную переменную
                        self.vr = self.collision_list.get(self.player)
                # если еще небыло коллизий то падаем вниз, если коллизия есть проверяем высоту прыжка
                # это защита от удержания клавиши прыжка
                elif self.vr != None:
                    # если клавиша прыжка удерживается, то мы проверяем высоту прыжка и 
                    # если она выше допустимого делаем y=0
                    if self.player.pos[1] > self.vr.pos[1] + 70:
                        self.player.vel_player_y = -2
        
        # проверяем запись в списке коллизий - если есть то проверяем на столкновение только этот блок
        elif self.collision_list.get(self.player):
        
            if self.player.collide_widget(self.collision_list[self.player]): 
                self.bjump = True

            # если коллизий больше нет - очищаем список коллизий и делаем скорость по x=0, y=-2
            else:
                self.collision_list.pop(self.player)
                self.player.vel_player_y = -2
                self.bjump = False

        # проверка на столкновение со стенами
        # ПРОБЛЕМА - если стоит у стены то при прыжке не падает вниз
        # - пока решил ее добовлением 5 пикселей при столкновении о стену
        # добавил отскок
        if self.player.collide_widget(self.blok_left):
            self.player.pos[0] = self.player.pos[0] + 4 
        elif self.player.collide_widget(self.blok_right):
            self.player.pos[0] = self.player.pos[0] - 4


    def collide_player(self, dt):
        """ функция коллизий персонажа с противником и бонусами"""

        apponet_collide = None# переменная в которую записываем противника с которым столкнулись
        # идем по списку аппонентов и проверяем на столкновение с ними
        for apponents in self.apponent_list.keys():
            
            # если столкнулись
            if apponents.collide_widget(self.player):
                # проверяем если жизнь не нулевая
                # то отнимаем 1 и присваиваем аппонента временной переменной по которой ниже его удоляем
                if self.player.coll_life != 0:
                    apponet_collide = apponents
                    self.player.coll_life -= 1
                # если жизнь 0 то всегда возвращаем персонажа на начало этажа
                else:
                    self.player.pos = (25, 115)
                    apponet_collide = apponents
        # создаем копию списка коллизий, проверяем кто из аппонентов столкнулся с персонажем
        # и затем удаляем этого аппанента из всех списков, 
        # затем удаляем и его 
        cort_copy = self.collision_list.copy()
        collide_corte = cort_copy.items()
        for corts in collide_corte:
            if corts[0] == apponet_collide:
                self.collision_list.pop(corts[0])
                self.apponent_list.pop(corts[0])
                self.remove_widget(corts[0])


    # функция загрузки скрина
    def on_enter(self, *args):

        # определение скорости персонажа
        self.player.vel_player_y = -2
        #print("player", self.player)

        # инициализация блоков
        # инициализируем постоянные блоки - пол и стены
        # первый блок записываем как обычно, а далее через функцию update
        self.blok_list = {self.blok_right: self.blok_right_name}
        self.blok_list.update({self.blok_left: self.blok_left_name})
        self.blok_list.update({self.blok_down: self.blok_down_name})

        # получаем блоки(список) из другого файла - функция спавна блоков и объеденяем списки
        #spawn_blok(self)
        levels.spawn_blok(self)
        self.blok_list.update(levels.spawn_blok(self))

        # установка блока перехода между уровнями
        blok_end = Blok_end(pos = levels.get_spawn_blok_end(self))
        self.blok_list.update({blok_end: blok_end.blok_end_name})
        self.add_widget(blok_end)

        # цвет окна
        Window.clearcolor = (1, 1, .8, 1)

        # спавн аппонентов, сколько аппонентов в секунду (сейчас один раз в 3 секунды)
        Clock.schedule_interval(self.spawn_apponent, 3 / 1) # в н сикунд / н раз
        # движение аппонента
        Clock.schedule_interval(self.move_apponent, 1 / 60.0)
        # движение игрока
        Clock.schedule_interval(self.mov_player, 1 / 60.0)
        # столкновение персонажа и аппонента
        Clock.schedule_interval(self.collide_player, 1 / 60.0)

    # функция выгрузки скрина
    def on_leave(self, *args):
        """ функция ухода с данного скрина (пауза) """
        # остановка таймера при смене скрина
        Clock.unschedule(self.move_apponent)
        Clock.unschedule(self.spawn_apponent)
        Clock.unschedule(self.mov_player)
        Clock.unschedule(self.collide_player) 