class Rectangle:
    # directly creating class properties
    # these are class level attributes and shared by all     instances
    height = 3
    width = 2
   # using constructor to create instance properties
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self): 
        return self.height * self.width
  