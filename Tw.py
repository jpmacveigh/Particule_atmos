# Créé par macveighjp, le 05/08/2014
# calcul itéatif de la température du thermomètre mouillé
from math import exp
L =2500. # J/g chaleur latente de vaporisation
Cp =1005. # J/kg/K chaleur spécifique à pression constante
PA = 2.53e+11 # Pa =
TB = 5.42e+3 # K
e = 0.622 # sans dimension
# P = pression Pa
# w = rapport de mélange en g(de vapeur)/kg (d'air sec)
# Tw = température du thermomètre mouillé en K
p=1015*100. # pression mesurée en Pa
w = 2. # rapport de mélange mesuré
Tw=18.+ 273.16 # valeur initiale = 10°C
for i in range(5):
    Twn = -L/Cp*(e*PA/p*exp(-TB/Tw) - w)
    Tw=Twn
    print Tw
