# Créé par jpmv, le 08/09/2014
import math
def bissection(f,x0,x1):
    """ Résolution de l'équation f(x)=0 par la méthode de la bissection.
    Réf : "Méthodes de calcul numérique" - J.P. Nougier 3ème édition
    editions Masson page 137.
    Il doit exister une solution unique dans l'interval l'interval [x0,x1] """
    epsilon=0.000001
    i=0
    while x1-x0>=2*epsilon:
        x2=1/2.*(x0+x1)
        x=f(x2)*f(x1)
        if x>0:
            x1=x2
        else:
            x0=x2
        i=i+1
    return (x0+x1)/2.
"""
def g(x):
    return x-math.cos(x)
print bissection(g,0.,1.)"""