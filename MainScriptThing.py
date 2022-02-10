from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from random import randint
from kivy.clock import Clock


class MyPaintWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cords = [0, 0]

    def on_touch_down(self, touch):
        with self.canvas:
            Color(randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255)

            d = 30.
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=10)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def newLine(self):
        with self.canvas:
            Color(randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255)
            self.cords[0] += 10
            d = 30.

            Line(points=((self.cords[0], 30), (203, self.cords[0])), width=10)


class MyPaintApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvasMandala = MyPaintWidget()

    def build(self):
        """
        return Button(
            text='hello boobs',
            pos=(0, 0),
            size_hint=(0.9, 0.9)
        )
        """

        Clock.schedule_interval(self.update, 0.0000001)

        return self.canvasMandala

    def update(self, *args):
        self.canvasMandala.newLine()


if __name__ == '__main__':
    MyPaintApp().run()

