# Créé par AD, le 14/09/2014

def gradientPseudoAbiabatiqueSature(temperature,pression,rapportDeMelangeSaturant):
    """ Calcul du gradient dT/dP dans une transformation pseudoadiabatique saturée. (A tester)
    Référence : "L'émagramme 761 des météorologue" - Bulletin de l'Union des Physiciens -
    Vol. 93 - juin 1999  pages 93-126 """
    R= 8,3144621    # constante universelle des gaz pafait en J/mol/K
    Ma=28.96        # masse molaire de l'air sec en g/mol
    Mv=18.          # masse molaire de la vapeur d'eau g/mol
    Lv= 40500.      # chaleur latente de vaporisation en J/mol (dépend de T) ??
    Cpa = 1004.     # chaleur massique de l'air sec à pression constante en J/kg/K
    Cprimev =  1410     # chaleur massique de la vapeur d'eau le long de la courbe de saturation en J/kg/K (dépend de T) ??

