# Créé par macveighjp, le 06/08/2014
import math
def tempe(ew):
    """ Calcul de la température (°C) en fonction de
    la pression de vapeur saturante (hPa) par inversion de la formule de Tetens
    formule de Tetens : ew=6.107*10**(7.5*temperature/(temperature+237.3)) """
    x = math.log10(ew/6.107)
    temperature = 237.3*x/(7.5-x)
    return temperature
#print tempe(12)