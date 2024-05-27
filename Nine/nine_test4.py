import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.uix.button import Button
from kivy.uix.label import Label


class Test_label(Label):
    def on_touch_down(self, touch):
        #return super().on_touch_down(touch)
        #NineTest.player.velocity = (2, 0)
        if self.collide_point(*touch.pos):
            #self.ids.player.velocity = (2, 0)
            print("касание Test_label", touch)

class Test_button(Button):
    def on_touch_down(self, touch):
        #return super().on_touch_down(touch)
        #NineTest.player.velocity = (2, 0)
        if self.collide_point(*touch.pos):
            #self.ids.player.velocity = (2, 0)
            print("касание Test_button", touch)


class Pers(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move_test(self):
        #self.velocity = (5, 0)
        self.pos = Vector(*self.velocity) + self.pos


class NineTest(Widget):
    player = ObjectProperty(None)

    btn = ObjectProperty(None)
    label1 = ObjectProperty(None)

    def on_touch_down(self, touch):
        if self.btn.collide_point(*touch.pos):
            self.player.velocity = (2, 0)
            print("касание player движется", touch)

        if self.label1.collide_point(*touch.pos):
            self.player.velocity = (-2, 0)
            print("касание player движется", touch)

    def on_touch_up(self, touch):
        #return super().on_touch_up(touch)
        if self.btn.collide_point(*touch.pos):
            self.player.velocity = (0, 0)
            print("убираем player стоп", touch)

        if self.label1.collide_point(*touch.pos):
            self.player.velocity = (0, 0)
            print("убираем player стоп", touch)

    #if btn.on_touch_down:
        #player.velocity = (-2, 0)


    def serve_player(self, vel=(0, 0)):
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