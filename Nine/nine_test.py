# File name: nine_test.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Blok(Widget):
    
    def blok_collide(self, player):
        if self.collide_widget(player):
            #player.velocity = (0, 0)
            player.pos = (200, 200)
            print("BAX", player.velocity)
        #print(player.pos)

class Blok2(Widget):
    pass

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

            if names == 'blok_poll' and self.velocity_y != 0:
                #self.pos = (200, 200)
                self.velocity = (2, 0)
                print("BAX-player", "blok_poll", self.velocity)

            if names == 'stop_label_n':
                #self.pos = (200, 200)
                self.velocity = (0, -2)
                print("BAX-player", "stop_label_n", self.velocity)
            
        #self.velocity = (0, -2)
        #print("нет коллизий")


class NineTest(Widget):
    player = ObjectProperty(None)
    blok = ObjectProperty(None)
    blok_base = ObjectProperty(None)
    blok_down = ObjectProperty(None)
    blok_down2 = ObjectProperty(None)
    blok_pol = ObjectProperty(None)
    stop_label = ObjectProperty(None)
    

    blok_right = 'blok_right'
    blok_left = 'blok_left'
    blok_bottom = 'blok_bottom'
    blok_poll = 'blok_poll'
    stop_label_n = 'stop_label'

    collision_list = DictProperty({})
    

    def serve_player(self, vel=(0, -2)):
        #self.player.center = self.center
        self.player.velocity = vel


    def update(self, dt):
        self.player.move()

        #self.player.player_collide(self.blok, self.blok_right)
        #self.player.player_collide(self.blok_base, self.blok_left)
        #self.player.player_collide(self.blok_down, self.blok_bottom)
        #self.player.player_collide(self.blok_pol, self.blok_poll)
        #self.player.player_collide(self.stop_label, self.stop_label_n)
        if self.player.collide_widget(self.blok):
            self.player.velocity_x *= -1
            print("Collide blok")

        elif self.player.collide_widget(self.blok_base):
            self.player.velocity_x *= -1
            print("Collide blok_base")
        
        elif self.player.collide_widget(self.blok_pol) and self.player.velocity_y != 0:
            self.player.velocity = (2, 0)
            print("Collide blok_pol")

        elif self.player.collide_widget(self.blok_down):
            if self.collision_list.get(self.player) != self.blok_down:
                self.collision_list[self.player] = self.blok_down
                self.player.velocity = (2, 0)
                print("Collide blok_down", self.collision_list)

        elif self.player.collide_widget(self.blok_down2):
            self.player.velocity = (2, 0)
            print("Collide blok_down2")

        elif self.player.collide_widget(self.blok_pol) == False:
            if self.collision_list.get(self.player):
                self.collision_list.pop(self.player)
                self.player.velocity = (0, -2)
                print("Collide NO", self.collision_list)

        #if self.player.collide_widget(self.stop_label):
            #self.player.velocity = (0, -2)
            #print("Collide stop_label")


class Nine_testApp(App):
    def build(self):
        game = NineTest()
        game.serve_player()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_testApp().run()