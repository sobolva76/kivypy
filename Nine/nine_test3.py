# File name: nine_test.py

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, DictProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.label import Label


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
    blok_pol = ObjectProperty(None)

    blok_down2 = ObjectProperty(None)

    stop_label = ObjectProperty(None)

    blok_test = ObjectProperty(None)
    blok_test2 = ObjectProperty(None)
    blok_list = DictProperty({})

    collision_list = DictProperty({})

    players_list = []

    rig_test = 1

    k = 0
    

    def serve_player(self, vel=(0, -2)):
        #self.player.center = self.center
        self.player.velocity = vel
        self.player2.velocity = vel
        self.players_list = [self.player, self.player2]

        blok = Blok(size = (10, 900), pos = (700, 0))
        #self.blok_list = [blok_test]
        self.blok_list.update({blok: 'blok'}) 
        self.add_widget(blok)

        blok_base = Blok(size = (10, self.height), pos = (0, 0))
        #self.blok_list = [blok_test]
        self.blok_list.update({blok_base: 'blok_base'})
        self.add_widget(blok_base)

        blok_down = Blok(size = (950, 10), pos = (100, 300))
        #self.blok_list = [blok_test]
        self.blok_list.update({blok_down: 'blok_down'}) 
        self.add_widget(blok_down)

        blok_test = Blok(size = (200, 10), pos = (10, 150))
        #self.blok_list = [blok_test]
        self.blok_list.update({blok_test: 'blok_test'}) 
        self.add_widget(blok_test)

        blok_test2 = Blok(size = (200, 10), pos = (100, 80))
        self.blok_list.update({blok_test2: 'blok_test2'})
        self.add_widget(blok_test2)
        #print("blok_list - ", self.blok_list)

        blok_pol = Blok(size = (700, 10), pos = (0, 0))
        self.blok_list.update({blok_pol: 'blok_pol'})
        self.add_widget(blok_pol)

        #stop_label = Label(text = "|", pos = (-30, 265), text_size = (5, 12))
        stop_label = Blok(size = (10, 10), pos = (70, 300))
        self.blok_list.update({stop_label: 'stop_label'})
        self.add_widget(stop_label)

        stop_label2 = Blok(size = (10, 10), pos = (320, 90))
        self.blok_list.update({stop_label2: 'stop_label'})
        self.add_widget(stop_label2)

        stop_label3 = Blok(size = (10, 10), pos = (220, 160))
        self.blok_list.update({stop_label3: 'stop_label'})
        self.add_widget(stop_label3)

        #print("blok_list - ", self.blok_list)


    def update(self, dt):

        for i in self.players_list:

            i.move()

            for blok_l in self.blok_list.keys():# проходим по списку блоков

            #print(self.players_list)
                #print("blok_list - ", self.blok_list)

                if i.collide_widget(blok_l):

                    #self.k = 0
                    #print("+collide+")

                    #print(self.blok_list.get(blok_l))

                    if self.blok_list.get(blok_l) == 'blok' or self.blok_list.get(blok_l) == 'blok_base':
                            i.velocity_x *= -1
                            print("Collide blok, blok_base")

                    elif self.collision_list.get(i) != blok_l:
                    
                        self.collision_list[i] = blok_l

                        i.velocity = (2, 0)
        
                        print("COLLISIA", self.collision_list)

                #else:
                    #if self.collision_list.get(i):
                        #self.collision_list.pop(i)
                        #i.velocity = (0, -2)
                        #print("Collide NO")

                    if self.blok_list.get(blok_l) == 'stop_label' and i.velocity_y == 0:
                        #print("stop_label")
                        if self.collision_list.get(i):
                            self.collision_list.pop(i)
                            i.velocity = (0, -2)
                            print("Collide NO", self.collision_list)
                #else:
                    #self.k += 1
                    #print(self.k)
                    #if self.k > 6:
                    #if self.collision_list.get(i):
                        #self.collision_list.pop(i)
                        #i.velocity = (0, -2)
                            #print("Collide NO", self.collision_list)

                    #if blok_l == self.blok or blok_l == self.blok_base:
                        #i.velocity_x *= -1
                        #print("Collide blok, blok_base")

                #elif i.collide_widget(self.blok_base):
                    #i.velocity_x *= -1
                    #print("Collide blok_base")
                
                #elif i.collide_widget(self.blok_pol) and i.velocity_y != 0:
                    #i.velocity = (2, 0)
                    #print("Collide blok_pol")

                    #elif blok_l == self.blok_pol and i.velocity_y != 0:
                        #i.velocity = (2, 0)
                        #print("Collide blok_pol")

                #elif i.collide_widget(self.blok_down):
                    #if self.collision_list.get(i) != self.blok_down:
                        #self.collision_list[i] = self.blok_down
                        #i.velocity = (2, 0)
                        #print("Collide blok_down", self.collision_list)

                #elif i.collide_widget(self.blok_down2):
                    #if self.collision_list.get(i) != self.blok_down2:
                        #self.collision_list[i] = self.blok_down2
                        #i.velocity = (2, 0)
                        #print("Collide blok_down2")

                #elif i.collide_widget(blok_l):
                    #if self.collision_list.get(i) != blok_l:
                        #self.collision_list[i] = blok_l
                        #i.velocity = (2, 0)
                        #print("Collide blok_test", self.collision_list)

                    

                        #elif self.blok_list.get(blok_l) == 'bok_pol' and i.velocity_y != 0:
                            #i.velocity = (2, 0)
                            #print("Collide blok_pol")

                        #elif self.blok_pol == False:
                            #if self.collision_list.get(i):
                                #self.collision_list.pop(i)
                                #i.velocity = (0, -2)
                                #print("Collide NO")

                        #else:
                            #i.velocity = (2, 0)
                            #print("Collide blok_test", self.collision_list)
                            #print("COLLISIA")

                    #elif self.collision_list.get(i):
                            #self.collision_list.pop(i)
                            #i.velocity = (0, -2)
                            #print("Collide NO", self.collision_list)

                #elif i.collide_widget(self.blok_pol) == False:
                    #if self.collision_list.get(i):
                        #self.collision_list.pop(i)
                        #i.velocity = (0, -2)
                        #print("Collide NO", self.collision_list)  

                    #elif self.blok_pol == False:
                        #if self.collision_list.get(i):
                            #self.collision_list.pop(i)
                            #i.velocity = (0, -2)
                            #print("Collide NO", self.collision_list)              


class Nine_test3App(App):
    def build(self):
        game = NineTest()
        game.serve_player()
        Clock.schedule_interval(game.update, 1 / 60.0)
        return game
    

if __name__ == '__main__':
    Nine_test3App().run()