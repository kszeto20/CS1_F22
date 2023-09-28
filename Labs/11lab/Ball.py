from tkinter import *

class Ball (object):
    def __init__(self, x, y, dx, dy, radius, color):
        self.x,self.y = x, y   # initial location
        self.radius = radius
        self.dx,self.dy = dx, dy    # the movement of the ball object
        self.color = color
            
    def position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def bounding_box(self):
        leftx = self.x - self.radius
        lefty = self.y - self.radius
        
        rightx = self.x + self.radius
        righty = self.y + self.radius
        
        return (leftx, lefty, rightx, righty)
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        if (0 < self.x + self.radius and \
              self.x - self.radius < maxx and \
              0 < self.y + self.radius and \
              self.y - self.radius < maxy):
            return True
        return False
    
    def check_and_reverse(self, maxx, maxy):
        changed = 0
        if self.x - self.radius <= 0 or self.x + self.radius >= maxx:
            self.dx = self.dx * -1
            changed = 1
        if self.y - self.radius <= 0 or self.y + self.radius >= maxy:
            self.dy = self.dy * -1
            changed = 1
        
        return changed == 1
            
            
