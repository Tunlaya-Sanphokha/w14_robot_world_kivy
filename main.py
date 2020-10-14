from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window

class Robot(Widget):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
    self._keyboard.bind(on_key_down = self._on_key_down)

    with self.canvas:
      self.robot = Rectangle(pos = (0,0) , size = (50,50))

  def _on_keyboard_closed(self):
    self._keyboard.unbind(on_key_down = self._on_key_down)
    self._keyboard = None

  def _on_key_down(self,keyboard,keycode,text,modifiers):
    x = self.robot.pos[0]
    y = self.robot.pos[1]
  
    if text == "w":
      y += 50
    if text == "s":
      y -= 50
    if text == "a":
      x -= 50
    if text == "d":
      x += 50

    self.robot.pos = (x,y)

class RobotWorld(App):
  def build(self):
    Window.size = (500,500)
    return Robot()

if __name__ == "__main__":
  RobotWorld().run()
