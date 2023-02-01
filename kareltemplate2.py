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

if __name__ == "__main__":
    run_karel_program()