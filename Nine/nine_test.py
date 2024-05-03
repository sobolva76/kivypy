# File name: nine_test.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.uix.label import Label


class Blok(Widget):
    
    def blok_collide(self, player):
        if self.collide_widget(player):
            player.velocity[0] = 0
            print("BAX")
        #print(player.pos)


class Player(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.velocity = (2, 0)
        self.pos = Vector(*self.velocity) + self.pos


class NineTest(Widget):
    player = ObjectProperty(None)
    blok = ObjectProperty(None)

    #def serve_player(self, vel=(2, 0)):
     #   self.player.center = self.center
      #  self.player.velocity = (3, 0)


    def update(self, dt):
        self.player.move()

        self.blok.blok_collide(self.player)


class Nine_testApp(App):
    def build(self):
        game = NineTest()
        #game.serve_player()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_testApp().run()