import re
import random

def chooseP(P,Q): 
    """
    for stochastic L systems
    P is the set of production rules; Q is the probabilities for each rule. 
    """
    x = random.random()
    q = 0 
    for i in range(0, len(P)): 
        q += Q[i]#add up probabilities 
        if x < q:#until you surpass the random event 
            return P[i]#at which point, return a production

def makeRegex(aDict):
    """ Build re object based on keys of supplied dict """
    return re.compile("|".join(map(re.escape, aDict)))

class D0LSystem:
    """ D0LSystem
        quasi-Deterministic L-system with 0 interactions. the system is context free

        input is a dict of productions and a dict of probabilities

        eg: grammar = {
            "A" : ["AB"],
            "B" : ["C", "D"] }
            probability = {
            "B" : [0.5, 0.5]}
        Originally written by Nick Porcino
        and found at http://meshula.net/wordpress/?p=6
    """
    def __init__(self, rules={}, prob={}):
        self.replaced = 0
        self.rules = rules
        self.rulesRegex = makeRegex(rules)
        for key in rules.keys():
            prob[key] = prob.get(key, [1])
#This assigns a probability of 1 to any production rule w/ prob. unassigned, making
#a production deterministic by default. Other ways of handling Det/Stok distinction?
#Other checks would be good, ie len(rules[i]) =?= len(prob[i]) and sum(prob[i]) =?= 1
        self.prob = prob

    def __call__(self, match):
        """ Handler called for each regex match """
        self.replaced += 1
        mash = match.group(0)
        if len(self.prob[mash]) == 1:
            return self.rules[mash][0]
        else:
            return chooseP(self.rules[mash], self.prob[mash])
#Again, other ways of handling this...

    def generate(self, text):
        """ Translate text, return modified text """
        self.replaced = 0
        # self is the first parameter, so that the __call__ method gets invoked
        return self.rulesRegex.sub(self, text)
    
    def generateX(self, text, x):
        """ Run x generations, return expanded rule, and 0 if the expansion was complete """
        self.replaced = 1
        while (self.replaced != 0 and x > 0):
            text = self.generate(text)
            x -= 1
        return (text, self.replaced)


def genotype(grammar, axiom, it, probability):
    next = D0LSystem(grammar, probability)
    (axiom, replacements) = next.generateX(axiom,it)
    return axiom#, replacements

#print genotype({'X':['S'], 'S':['XS','SX']}, 'X', 10, {'S':[0.5,0.5]})

