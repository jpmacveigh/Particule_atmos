def ew (temperature):
    """ Calcul de la pression de vapeur saturante (hPa)
        en fonction de la température (°C) par la formule de Tetens
        formule de Tetens:  ew=6.107*10**(7.5*temperature/(temperature+237.3))
        Permet de calculer,  par définition de sa température du point de
        rosée Td, la pression de vapeur d'une particule = e=ew(Td).   """
    ew=6.107*10**(7.5*temperature/(temperature+237.3))
    return ew
#print ew(10) # pression de vapeur saturante avec T = 10°c
#print ew(8)  # pression de vapeur avec Td= 8 °C