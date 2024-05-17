# File name: nine_test.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Blok(Widget):
    pass

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
        

class NineTest(Widget):
    player = ObjectProperty(None)
    player2 = ObjectProperty(None)

    blok = ObjectProperty(None)
    blok_base = ObjectProperty(None)
    blok_down = ObjectProperty(None)
    blok_down2 = ObjectProperty(None)
    blok_pol = ObjectProperty(None)
    stop_label = ObjectProperty(None)

    collision_list = DictProperty({})

    players_list = []
    

    def serve_player(self, vel=(0, -2)):
        #self.player.center = self.center
        self.player.velocity = vel
        self.player2.velocity = vel
        self.players_list = [self.player, self.player2]


    def update(self, dt):

        for i in self.players_list:

            i.move()

            #print(self.players_list)

            if i.collide_widget(self.blok):
                i.velocity_x *= -1
                print("Collide blok")

            elif i.collide_widget(self.blok_base):
                i.velocity_x *= -1
                print("Collide blok_base")
            
            elif i.collide_widget(self.blok_pol) and i.velocity_y != 0:
                i.velocity = (2, 0)
                print("Collide blok_pol")

            elif i.collide_widget(self.blok_down):
                if self.collision_list.get(i) != self.blok_down:
                    self.collision_list[i] = self.blok_down
                    i.velocity = (2, 0)
                    print("Collide blok_down", self.collision_list)

            elif i.collide_widget(self.blok_down2):
                i.velocity = (2, 0)
                print("Collide blok_down2")

            elif i.collide_widget(self.blok_pol) == False:
                if self.collision_list.get(i):
                    self.collision_list.pop(i)
                    i.velocity = (0, -2)
                    print("Collide NO", self.collision_list)


class Nine_test3App(App):
    def build(self):
        game = NineTest()
        game.serve_player()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_test3App().run()