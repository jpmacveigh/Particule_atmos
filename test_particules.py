from Particule import Particule
p=Particule(700.,5.,-6.) # Triplet - Roche page 72
p.affiche()
pnew=p
# détente adiabatique jusqu'à saturation (T devient < Td)
for i in range (420):
    pnew=pnew.transfAdiabSeche(-.5) # détente de 0.5 hPa
    print i
    pnew.affiche()
