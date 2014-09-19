# Créé par jpmv, le 06/08/2014
def rapDeMelange (pression,e):
    """ Calcul du rapport de mélange (g de vapeur d'eau/kg d'air sec)
    en fonction de la pression (hPa) et de la tension de vapeur (hPa)  """
    rapport= 1000.*0.622*e/(pression-e)  # *1000. pour avoir des g/kg
    return rapport
#print rapDeMelange (1000.,18.)