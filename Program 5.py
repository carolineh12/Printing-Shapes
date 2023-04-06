#parallelogram; if have three rows, shift first one over 2, second one over 1, third one no shift
#constructor; if <=0 make it equal to 1
#if p1.width = -1, keep the width at what it was already set at(ignore)   

class Shape:
    def __init__(self, w=1, h=1):
        self.width = w
        self.height = h
    
    @property 
    def width(self): 
        return self._width
    @width.setter
    def width(self, w):
        if w <= 0:
            self._width = 1
        else:
            self._width = w
    @property 
    def height(self): 
        return self._height
    @height.setter
    def height(self, h):
        if h <= 0:
            self._height = 1
        else:
            self._height = h
    def __str__(self):
        image = ""
        for i in range(self.height):
            image += ("* " * self.width) + "\n"
        return image 
        
class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)
        
class Square(Shape):
    def __init__(self, w):
        super().__init__(w, w) #passing in l for l and w in the shape constructor 

class Triangle(Shape):
    def __init__(self, w):
        super().__init__(w, w)
    
    def __str__(self):
        image = ""
        for i in range(self.height):
            image += ("* " * (self.height - i)) + "\n"
        return image

class Parallelogram(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)
    
    def __str__(self):
        image = ""
        shift = self.height 
        for i in range(self.height):
            image += "  " * shift + "* " * (self.width) + "\n"
            shift -=1
        return image 

        
        
    



#MAIN PROGRAM
r1 = Rectangle(12, 4)
print(r1)
s1 = Square(6)
print(s1)
t1 = Triangle(7)
print(t1)
p1 = Parallelogram(10, 3)
print(p1)
r2 = Rectangle(0, 0)
print(r2)
p1.width = 2
p1.width = -1
p1.height = 2
print(p1)

