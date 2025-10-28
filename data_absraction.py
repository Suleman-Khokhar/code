############################################################
"""                  DATA Abstraction              """
############################################################
## Def: 
##     Hiding the deatils and showing the necessary only >>>>
##      Separatng how data is represented and from how it is manipulated >>>>>
#Example:

# 1) expression :  

pi = 22/7
radius = 2
area =     pi*(radius **2)     

# 2) Function :

def add(n_1,n_2):
    return n_1 + n_2

n_1 = 3 
n_2 = 2
result = add(n_1,n_2)
print(result)

##############################3
"""1. Representated :"""

def rational(x,y):
#   return {"numinator: x, denominnator:y"}
    return [x,y]

def num(x):
    return x[0]

def denom(x):
    return x[1]

"""2. Separation :"""

def add_rational(x,y):
    return [(x[0]*y[1])+(x[1]*y[0]),x[1]*y[1]]

def mult_rational(x,y):
    return (x[0]*y[0],x[1]*y[1])


## so separation are done by function 
##  add_rational , mult_rational , .....


def print_rational(x):
    return f"{num(x)}/{denom(x)}"

r1 = rational(1,2)
r2 = rational(1,3)
result = add_rational(r1,r2)
print(print_rational(result))

######################################

## Abstraction baarier

def add_rational(x,y):
    return [(num(x)*denom(y))+(denom(x)*num(y)),num(x)*denom(y)]

def mult_rational(x,y):
    return (num(x)*num(y),denom(x)*denom(y))



