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
    
    #blok_end = Blok_end(pos = (650, 155))
    #blok_list_levels = {blok_end: blok_end.blok_end_name}
    #self.add_widget(blok_end)

    return blok_list_levels