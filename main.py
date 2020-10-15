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
      Color(0, 250., 0)
      for i in range (0,1) :
      	for j in range (2,10) :
      	  self.barrier = Rectangle(pos = (j*50,i*50) , size = (50,50))
      	  self.position[i][j] = 1
      	  
      for i in range (2,10) :
      	for j in range (0,1) :
         self.barrier = Rectangle(pos = (j*50,i*50) , size = (50,50))
         self.position[i][j] = 1
         
      for i in range (3,5) :
      	for j in range (3,10,2) :
      	  self.barrier = Rectangle(pos = (j*50,i*50) , size = (50,50))  
      	  self.position[i][j] = 1
      	  
      for i in range (3,10,2) :
      	for j in range (3,5) :
      	  self.barrier = Rectangle(pos = (j*50,i*50) , size = (50,50))	
      	  self.position[i][j] = 1
      	   
      Color(0, 0, 250.)
      self.target = Rectangle(pos = (450,450) , size = (50,50))
      self.position[9][9] = 2
  
  def _on_keyboard_closed(self):
    self._keyboard.unbind(on_key_down = self._on_key_down)
    self._keyboard = None
    
  def _on_key_down(self,keyboard,keycode,text,modifiers):
    row = self.robot.pos[1]
    column = self.robot.pos[0]

    if text == "w":
      if row + 50 >=500 :
         pass
      elif self.position[int(row+50)//50][int(column)//50] == 1:
         pass
      else :
         row += 50
         
    if text == "s":
      if row - 50 < 0 :
         pass
      elif self.position[int(row-50)//50][int(column)//50] == 1:
         pass
      else :
         row -= 50
         
    if text == "a":
      if column - 50 < 0 :
         pass
      elif self.position[int(row)//50][int(column-50)//50] == 1:
         pass
      else :
         column -= 50
         
    if text == "d":
      if column + 50 >=500 :
         pass
      elif self.position[int(row)//50][int(column+50)//50] == 1:
         pass
      else :
         column += 50
         
    self.robot.pos = (column,row)
    
    print(self.position)
    print(int(row)//50,int(column)//50) 
    print(self.position[int(row)//50][int(column)//50])
    
    
class RobotWorld(App):
  def build(self):
    Window.size = (500,500)
    return World() 

if __name__ == "__main__":
  RobotWorld().run()


