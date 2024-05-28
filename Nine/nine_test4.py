import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.uix.button import Button
from kivy.uix.label import Label


class Blok(Widget):
    pass


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
    btn2 = ObjectProperty(None)
    btn3 = ObjectProperty(None)

    blok = ObjectProperty(None)

    blok_list = DictProperty({})

    

    def on_touch_down(self, touch):
        if self.btn.collide_point(*touch.pos):
            self.player.velocity = (2, 0)
            print("касание player движется", touch)

        if self.btn2.collide_point(*touch.pos):
            self.player.velocity = (-2, 0)
            print("касание player движется", touch)

        if self.btn3.collide_point(*touch.pos):
            self.player.velocity_y = 28
            print("касание player движется", touch)

    def on_touch_up(self, touch):
        #return super().on_touch_up(touch)
        if self.btn.collide_point(*touch.pos):
            self.player.velocity = (0, 0)
            print("убираем player стоп", touch)

        if self.btn2.collide_point(*touch.pos):
            self.player.velocity = (0, 0)
            print("убираем player стоп", touch)

        if self.btn3.collide_point(*touch.pos):
            self.player.velocity = (0, 0)
            print("убираем player стоп", touch)


    def serve_player(self, vel=(0, 0)):
        self.player.velocity = vel

        blok = Blok(size = (900, 10), pos = (0, 50))
        #self.blok_list = [blok_test]
        self.blok_list.update({blok: 'blok'}) 
        self.add_widget(blok)
        print(self.blok_list)

    
    def update(self, dt):
        self.player.move_test()
        
        for blok_l in self.blok_list.keys():
            if self.player.collide_widget(blok_l):
                self.player.velocity_y = 0
                print("COLLIDE")
            else:
                self.player.velocity = (0, -2)

            #print(self.blok)


class Nine_test4App(App):
    def build(self):
        game = NineTest()
        game.serve_player()
        Clock.schedule_interval(game.update, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_test4App().run()