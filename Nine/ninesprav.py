import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window


class Ninesprav(Widget):
    def __init__(self, **kwargs):
        super(Ninesprav, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)

    def _keyup(self,*args):
        print(args)

    def _keydown(self,*args):
        print(args)

# класс запуска приложения
class NinespravApp(App):
    def build(self):
        game = Ninesprav()
    
        #Clock.schedule_interval(game.spawn_apponent, 3 / 1) # в н сикунд / н раз

        return game
    

if __name__ == '__main__':
    NinespravApp().run()