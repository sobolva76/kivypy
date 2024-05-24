import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Pers(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    velocity = (2, 0)
    
    def move_test(self):
        #self.velocity = (5, 0)
        self.pos = Vector(*self.velocity) + self.pos


class NineTest(Widget):
    player = ObjectProperty(None)

    btn = ObjectProperty(None)

    #def on_touch_down(self, touch):
        #return super().on_touch_down(touch)
        #self.player.velocity = (2, 0)
        #print("касание", touch)

    if btn.on_touch_down:
        player.velocity = (-2, 0)


    def serve_player(self, vel=(0, 2)):
        self.player.velocity = vel

    
    def update(self, dt):
        self.player.move_test()


class Nine_test4App(App):
    def build(self):
        game = NineTest()
        game.serve_player()
        Clock.schedule_interval(game.update, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_test4App().run()