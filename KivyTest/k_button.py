from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'resizable', True)

from kivy.clock import Clock
from kivy.animation import Animation


class BaseLayout(BoxLayout):
    def say_Hello(self):
        print("Hello")


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.breath, 1)

    def breath(self, btx):
        anim = (Animation(btn_size = (60, 60), t = 'in_quad', duration = 0.5) +
                Animation(btn_size = (70, 70), t = 'in_quad', duration = 0.5))
        
        tgt = self.ids.cta
        anim.start(tgt)


class K_buttonApp(App):
    def build(self):
        return BaseLayout()
        #return MainWindow()
     

if __name__ == '__main__':
    K_buttonApp().run()