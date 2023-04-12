####################################################################
# Shapes
# Liz Denson & Caroline Holland
# Last modified on 2023-04-12
#
# An object-oriented program that implements inheritance.
####################################################################

# Shape class
class Shape:
    
    # Initializes the Shape class with width and height parameters
    def __init__(self, w=1, h=1):
        self._width = w if w > 0 else 1
        self._height = h if h > 0 else 1
        
    # Width getter
    @property
    def width(self): 
        return self._width
    
    # Width setter
    @width.setter
    def width(self, w):
        if w > 0:
            self._width = w
            
    # Height getter
    @property 
    def height(self): 
        return self._height
    
    # Height setter
    @height.setter
    def height(self, h):
        if h > 0:
            self._height = h
            
    # __str__ method to view the shape as a string
    def __str__(self):
        image = ""
        for i in range(self.height):
            image += ("* " * self.width) + "\n"
        return image
    
# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)
        
# Square class inheriting from Shape
class Square(Shape):
    def __init__(self, w):
        super().__init__(w, w) # Passes w as both width and height in the Shape constructor
        
# Triange class inheriting from Shape
class Triangle(Shape):
    def __init__(self, w):
        super().__init__(w, w)
        
    # __str__ method to view the Triangle as a string
    def __str__(self):
        image = ""
        for i in range(self.height):
            image += ("* " * (self.height - i)) + "\n"
        return image
    
# Parallelogram class inheriting from Shape
class Parallelogram(Shape):
    def __init__(self, w, h):
        super().__init__(w, h) # Calls the Shape constructor
        
    # __str__ method to view the Parallelogram as a string
    def __str__(self):
        image = ""
        shift = self.height 
        for i in range(self.height):
            image += "  " * shift + "* " * (self.width) + "\n"
            shift -= 1
        return image
    
###############
# MAIN PROGRAM
###############

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
