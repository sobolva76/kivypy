# file levels_1.py - первый уровень
import kivy
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.lang import Builder

#Builder.load_file('levels_1.kv')


class Blok_base(Widget):
    """ класс блоков расположенных на уровне (не включая пол и стены) """
    blok_base_name = "blok_base"


class Blok_end(Widget):
    """ Класс перехода между этажами """
    blok_end_name = "blok_end"
    

blok_list_levels = DictProperty({})# список блоков


def spawn_blok(self):

    blok_base = Blok_base(size = (100, 10), pos = (550, 150))
    blok_list_levels = {blok_base: blok_base.blok_base_name}
    self.add_widget(blok_base)
    
    blok_base = Blok_base(size = (500, 10), pos = (10, 150))
    blok_list_levels.update({blok_base: blok_base.blok_base_name})
    self.add_widget(blok_base)

    blok_base = Blok_base(size = (700, 10), pos = (200, 200))
    blok_list_levels.update({blok_base: blok_base.blok_base_name})
    self.add_widget(blok_base)

    blok_base = Blok_base(size = (300, 10), pos = (10, 250))
    blok_list_levels.update({blok_base: blok_base.blok_base_name})
    self.add_widget(blok_base)
    
    return blok_list_levels


def get_spawn_blok_end(self):
    """ установка перехода между этажами - возвращает кортеж (x, y)"""
    #blok_end = Blok_end(pos = (650, 155))
    #blok_list_levels = {blok_end: blok_end.blok_end_name}
    #self.add_widget(blok_end)
    return (650, 155)

# геттеры и сетеры для уровня

def get_koll_point_spawn(self):
    """ геттер колличества точек спавна противника"""
    koll_point_spawn = 2
    return koll_point_spawn

def get_koll_spawn(self):
    """ геттер колличества противников на уровне"""
    koll_spawn = 4
    return koll_spawn

def get_spawn_apponent_l(self):
    """ геттер координат спавна с лева - возврящает кортеж из (x, y) """
    koord_spawn_apponent_l = (50, 500)
    return koord_spawn_apponent_l


def get_spawn_apponent_r(self):
    """ геттер координат спавна с права - возврящает кортеж из (x, y) """
    koord_spawn_apponent_r = (500, 500)
    return koord_spawn_apponent_r