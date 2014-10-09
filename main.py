
from genotype import genotype
from phenotype import phenotype
#import turtle

grammar = {     "F" : ["F[+F][-F]"]    
}

probability = {
}

axiom = "F"

it = 4#iteration number


gene = genotype(grammar, axiom, it, probability)
print gene
phenotype(gene)


