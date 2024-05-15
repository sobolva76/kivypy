# File name: nine_test.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Blok(Widget):
    
    def blok_collide(self, player):
        if self.collide_widget(player):
            #player.velocity = (0, 0)
            player.pos = (200, 200)
            print("BAX", player.velocity)
        #print(player.pos)


class Player(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """ функция движения персонажа """
        #self.velocity = (2, 0)
        self.pos = Vector(*self.velocity) + self.pos

    
    def player_collide(self, blok, names):
        """ функция определения столкновений персонажа с предметами
        blok - любой виджет 
        """
        #print("Collide")
        if self.collide_widget(blok):
            if names == 'blok_right':
                #self.pos = (200, 200)
                self.velocity_x *= -1
                print("BAX-player", "blok_right", self.velocity)

            if names == 'blok_left':
                #self.pos = (200, 200)
                self.velocity_x *= -1
                print("BAX-player", "blok_left", self.velocity)
                
            if names == 'blok_bottom' and self.velocity_y != 0:
                #self.pos = (200, 200)
                self.velocity = (2, 0)
                print("BAX-player", "blok_bottom", self.velocity)

        else:
            self.velocity = (0, -2)
            print("нет коллизий")


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

        #self.blok.blok_collide(self.player) 
        #self.blok_height.blok_collide(self.player) 
        self.player.player_collide(self.blok, self.blok_right)
        self.player.player_collide(self.blok_base, self.blok_left)
        self.player.player_collide(self.blok_down, self.blok_bottom)


class Nine_testApp(App):
    def build(self):
        game = NineTest()
        game.serve_player()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_testApp().run()