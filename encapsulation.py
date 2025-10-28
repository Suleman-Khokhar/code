############################################################
"""                  DATA Encapsulation               """
############################################################

## Data Absraction is simply a method of divided a process in to layers of functions 
### Data Encapsulation is the method of applying lock  on that layers 
  

## Objects are black boxes with unique id's

### l1 = [1,3]
### l2 = [1,3]
### l1 == l2 --> false 

# so objects are also different if they have same data .......

######################################################

                              ## Data Abscration ##
def make_point(x,y):
    return [x,y]
def get_x(P):
    return P[0]
def get_y(P):
    return P[1]
def distance(p1,p2):
    return ((get_x(p1)-get_x(p2)**2)+(get_y(p1)-get_y(p2)**2))**0.05
def is_within(point,center,radius):
    return distance(point,center)<=radius

######################################################
###
##### clouser function
###
"""                     Data Encapsulation                  """
def fun():
    N = 8
    return True

## There is no way to access the N variable and its value 
### so to make function inaccessable we make clouser functions
### clouser function remamber the parent function variable and remian for a long time in fram if the parent frame is deleted 
 
## syntax :
def function():
    def fun():
        return True
    return fun

##Example :
def make_adder(x):
    def add_5(y):
        return x+y
    return add_5
add =  make_adder(10)
print(add(5))

########################
def make_points(x,y):
    def points():
        return [x,y]
    def set_x(new_x):
        nonlocal x
        x =new_x
    return points,set_x

P , set_x = make_points(1,2)
print(P())
set_x(6)
print(P())

## example:
def Make_points(x,y):
    def make_point():
        return [x,y]
    def get_x(P):
        return P[0]
    def get_y(P):
        return P[1]
    def distance(p1,p2):
        return ((get_x(p1)-get_x(p2)**2)+(get_y(p1)-get_y(p2)**2))**0.05
    def is_within(point,center,radius):
        return distance(point,center)<=radius
    return  distance, is_within
    # return make_point, get_x, get_y, distance, is_within

###################### Through dictionary 
def Make_points(x,y):
    def make_point():
        return [x,y]
    def get_x():
        return x
    def get_y():
        return y
    def distance(other_point):
        return (( get_x()- other_point["get_x"]()**2 ) + ( get_y()-other_point["get_y"]()**2))**0.05
    def is_within(point,center,radius):
        return distance(point,center)<=radius
    return  {
             "get_x()" : get_x,
             "get_y"   : get_y,
             "distance":  distance,
             "is_within": is_within
            }
    # return make_point, get_x, get_y, distance, is_within

P = Make_points(1,2)

# type(P) ---> dictionary
# type(P["get_x"]) --> function so can be used as : P["get_x"]() 

