from stanfordkarel import *


class ktools:
def m(self):
  """Shorthand for move"""
  move()
  
def tl(self):
  """turn left"""
  turn_left()
  
def tr(self):
  """turn right"""
  self.tl()
  self.tl()
  self.tl()
  
def ta(self):
  """Turn around"""
  self.tl()
  self.tl()

def pick(self):
  """pick beeper"""
  pick_beeper()

def put(self):
  """put beeper"""
  put_beeper()

def put2(self):
  """put two beepers in a line"""
  self.put()
  self.m()
  self.put()

def put5(self):
  """put five beepers in a line"""
  self.put2()
  self.m()
  self.put2()
  self.m()
  self.put()

def h(self):
  """print H using beepers"""
  self.tl()
  self.put5()
  self.tr()
  self.m()
  self.m()
  self.m()
  self.tr()
  self.put5()
  self.ta()
  self.m()
  self.m()
  self.tl()
  self.put2()
  self.tl()
  self.m()
  self.m()
  self.tl()
  self.m()
  self.m()
  self.m()
  self.m()

def e(self):
  """Print E using beepers"""

def l(self):
  """Print L using beepers"""

def o(self):
  """Print O using beepers"""

  
def main():
    """Karel code goes here!"""
    kt = ktools()
    pass

def fic(self):
  """Front is clear"""
  return front_is_clear()

def fib(self):
  """Front is blocked"""
  return front_is_blocked()

def ric(self):
  """Right is clear"""
  self.tr()
  if self.fic(): 
    self.tl()
    return True #immediately exit the function
  self.tl()
  return False 

def rib(self):
  """Right is blocked"""
  return not self.ric()

def mazemove(self):
  """Maze move"""
  if self.fib()
    self.tl()
else:  #Otherwise...
  self.m()
  if self.ric()
    self.tr()
    self.m()
    if self.ric()
      self.tr()
      self.m()
pass

def mm(self, num):
  """move multiple"""
  for number in range(num):
    self.m()


def pickm(self, num):
  """Pick multiple"""
  for step in range(num-1):
    self.pick()
    self.m()
  self.pick()

def putm(self, num):
  """put multiple"""
  for _ in range(0, num-1):
    self.put()
    self.m()
  self.put()

if __name__ == "__main__":
    run_karel_program()