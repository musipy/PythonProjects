import math
class Shape:
    def __init__(self, height, width):
        self.height=height
        self.width=width
    def __repr__(self):
        return ('<' + self.__class__.__name__+' x='+str(self.height)+' y='+str(self.width)+'>')
    
class Circle(Shape):
    def __init__(self, height, width, radius):
        super().__init__(height, width)
        self.radius=radius
    def __repr__(self):
        return ('<' + self.__class__.__name__+' x='+str(self.height)+' y='+str(self.width)+' radius='+str(self.radius)+'>')
    def area(self):
        return (((self.radius)*(self.radius))*math.pi)
    def circumference(self):
        return(2*math.pi*self.radius)

class Rectangle(Shape):
    def __init(self, height, width):
        super().__init__(height, width)
    def __repr__(self):
        return ('<' + self.__class__.__name__+' x='+str(self.height)+' y='+str(self.width)+'>')
    def area(self):
        return(self.height*self.width)
    def circumference(self):
        return((2*self.height)+(2*self.width))
    
class RightTriangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)
    def __repr__(self):
        return ('<' + self.__class__.__name__+' x='+str(self.height)+' y(base)= '+str(self.width)+'>')
    def area(self):
        return((self.height*self.width)/2)
    def circumference(self):
        return(math.sqrt((self.height*self.height)+(self.width*self.width))+self.height+self.width)

class Square(Rectangle):
    def __init(self, height, width):
        super().__init__(height, width)
        


        
