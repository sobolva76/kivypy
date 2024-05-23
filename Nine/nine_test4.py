import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Pers(Widget):

    speed = 1
    
    def move_test(self):
        self.pos[0] += self.speed

    def speed_pers(self):
        self.speed = 10


class NineTest(Widget):
    player = ObjectProperty(None)


class Nine_test4App(App):
    def build(self):
        game = NineTest()
        #game.serve_player()
        #Clock.schedule_interval(game.update, 1 / 60.0)
        #Clock.schedule_interval(Pers.move_test, 1 / 60.0)
        Pers.speed_pers(self)
        return game
    

if __name__ == '__main__':
    Nine_test4App().run()