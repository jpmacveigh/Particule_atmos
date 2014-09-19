def tVap (pression,rapMelange):
    """ Calcul de la tension de vapeur (hPa) d'une particule d'air humide
    en fonction de sa pression (hPa) et de son rapport de mélange (g/Kg) """
    rap=rapMelange/1000.  # transformation en g/g
    tVap=pression*rap/(0.622+rap)
    return tVap
#print tVap(1000,11.401)