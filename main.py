from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window

class World(Widget):

  position = [ [0 for i in range(10) ] for j in range(10) ]
  
  for i in range (10):
    for j in range (10):
      position[i][j] = 0
      
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
    self._keyboard.bind(on_key_down = self._on_key_down)

    with self.canvas:
      Color(250., 0, 0)
      self.robot = Rectangle(pos = (0,0) , size = (50,50))

  
  def _on_keyboard_closed(self):
    self._keyboard.unbind(on_key_down = self._on_key_down)
    self._keyboard = None
    
  def _on_key_down(self,keyboard,keycode,text,modifiers):
    row = self.robot.pos[1]
    column = self.robot.pos[0]

    if text == "w":
      row += 50
    if text == "s":
      row -= 50
    if text == "a":
      column -= 50
    if text == "d":
      column += 50

    self.robot.pos = (column,row)
    
    print(self.position)

class RobotWorld(App):
  def build(self):
    Window.size = (500,500)
    return World() 

if __name__ == "__main__":
  RobotWorld().run()

