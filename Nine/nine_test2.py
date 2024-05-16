# File name: nine_test.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Blok(Widget):
    
    def blok_collide(self, player, names):
        if self.collide_widget(player):
            #player.velocity = (0, 0)
            #player.pos = (200, 200)
            #print("BAX", player.velocity)
            #print(player.__dict__)

            if names == 'blok_right':
                #self.pos = (200, 200)
                player.velocity_x *= -1
                print("BAX-blok", "blok_right", player.velocity)

            if names == 'blok_left':
                #self.pos = (200, 200)
                player.velocity_x *= -1
                print("BAX-blok", "blok_left", player.velocity)
                
            if names == 'blok_bottom' and player.velocity_y != 0:
                #self.pos = (200, 200)
                player.velocity = (2, 0)
                print("BAX-blok", "blok_bottom", player.velocity)
            elif names == 'blok_bottom' and player.velocity_y == 0:
                player.velocity_x = player.velocity_x
        else:
            print("NO COLLIDE")
            #player.velocity = (0, -2)


class Player(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """ функция движения персонажа """
        #self.velocity = (2, 0)
        self.pos = Vector(*self.velocity) + self.pos

    
class NineTest(Widget):
    player = ObjectProperty(None)
    blok = ObjectProperty(None)
    blok_base = ObjectProperty(None)
    blok_down = ObjectProperty(None)
    

    blok_right = 'blok_right'
    blok_left = 'blok_left'
    blok_bottom = 'blok_bottom'
    

    def serve_player(self, vel=(0, -2)):
        #self.player.center = self.center
        self.player.velocity = vel


    def update(self, dt):
        self.player.move()

        self.blok.blok_collide(self.player, self.blok_right) 
        self.blok_base.blok_collide(self.player, self.blok_left) 
        self.blok_down.blok_collide(self.player, self.blok_bottom)
        

class Nine_test2App(App):
    def build(self):
        game = NineTest()
        game.serve_player()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_test2App().run()