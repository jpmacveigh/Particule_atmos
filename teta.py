# Créé par macveighjp, le 06/08/2014
def teta (pression,temperature):
    """ Calcul de la température potentielle (°C) en fonction de
    la pression(hPa) et de la température (°C) """
    Ra  = 287.  # constante spécifique gaz parfait air sec (J/kg/°K)
    Cpa = 1005. # chaleur massique à pression constante air sec (J/kg/°K)
    teta = (temperature+273.15)*((1000./pression)**(Ra/Cpa))
    return teta-273.15
#print teta(850,10)