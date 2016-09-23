from kivy.app import App
from kivy.uix.widget  import Widget
from kivy.graphics import Line


class Draw(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x,touch.y))
            touch.ud["line2"] = Line(points=(touch.x,touch.y+30))

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x,touch.y)
        touch.ud["line2"].points += (touch.x,touch.y+30)

        print (touch.ud["line"].points)


class FirstKivy(App):
    def build(self):
        return Draw()


if __name__ == "__main__":
    FirstKivy().run();
