from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView


class BaseLayout(BoxLayout):
    pass

class ProgBar(BoxLayout):
    pass


class SliderWidget(BoxLayout):
    pass

class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(5)]


class Background(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass



class K_base2App(App):
    def build(self):
        return Background()
    

if __name__ == '__main__':
    K_base2App().run()