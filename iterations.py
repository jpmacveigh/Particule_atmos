# Créé par macveighjp, le 05/08/2014
from math import exp
""" imprime la suite des X(n)= X(n-1)**2
    avec X(0)=2  """
x=2
for i in range(6) :
    xs=x**2
    x=xs
    print x
