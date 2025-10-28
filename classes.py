############################################################
"""                  Classes in python            """
############################################################

# syntax:
## class_keyword    class_name :
  
class Class_name:
    def __init__(self):
        pass
 
 ################ SO basically self is a paramemter that invoke a function using dot 

#Example:
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def prints(self):
        print(f"{self.get_x()},{self.get_y()}")
        
P = Point(1,2)
P.prints()
