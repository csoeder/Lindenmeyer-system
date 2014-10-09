import turtle

###Graph utilities################
#from pygraph.classes.graph import graph



##################################
class move:
#"""
#defines a function which consists of turtle actions, etc. 
#"""

    def __init__(self, angle=0, dist = 10, **kwargs):
        self.angle = angle
        self.dist = dist
        self.kwargs = kwargs

    def __call__(self, dummy, char=1.0, **kwargs):
#        def moo(dummy, char=1):#characteristic length of 1; use this to control eg power law growth; dummy is the string which gets processed. 
        if 'color' in self.kwargs:
            turtle.color(self.kwargs['color'])
        elif 'color' in kwargs:
            turtle.color(kwargs['color'])
        else:
            turtle.color('black')
        turtle.rt(self.angle)#turtle's angle set first, measured from the right
        turtle.fd(char*self.dist)#then the turtle moves 
            
        return dummy[1:]#discard the character just drawn.
        
###############################


def split(wholeStr, subStr):
    for i in range(0, len(wholeStr)-len(subStr)+1):
    	if wholeStr[i:i+len(subStr)]== subStr:
    		return wholeStr[0:i], wholeStr[i+len(subStr)-1:]
    return wholeStr, ""

turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.width(5)
eff = move(0, 10*2.5, color='blue')
ess = move(0, 7.5*2.5, color='red')
minus = move(23, 0)
plus = move(-29, 0)
sym = move(360/7,0)#n-fold symmetry

def push(dummy):
    global stack
    stack += [(turtle.pos(), turtle.heading())]
    [recurse, residue] = split(dummy, "]")
    phenotype(recurse[1:])
    return residue
def pop(dummy):
    global stack
    turtle.up()
    turtle.goto(stack[-1][0])
    turtle.seth(stack[-1][1])
    stack = stack[:-1]
    turtle.down()
    return dummy[1:]

stack = []


parse_dict = {"F" : eff, "[": push, "]": pop, "+":plus, "-":minus, "*":sym, "S":ess}
##is this where i want this?

def phenotype(word):
    while len(word) > 0:
        word = parse_dict[word[0]](word)

