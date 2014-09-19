# Créé par macveighjp, le 06/08/2014
import math
from ew import ew
from teta import teta
from rapDeMelange import rapDeMelange
from tVap import tVap
from tempe import tempe
from bissection import bissection
class Particule:
    """ Une particule d'air atmosphérique humide
        définie par sa pression (hPa), température (°C) et sa
        température du point de rosée (°C)      """
    def __init__ (self,pression,temperature,temperaturePointDeRosee):
        self.pression=pression
        self.temperature=temperature
        self.temperaturePointDeRosee=temperaturePointDeRosee
        """if self.temperaturePointDeRosee > self.temperature :
            self.affiche()
            raise ValueError("Td est > T")"""
    def transfAdiabSeche(self,dp):
        """ Retourne une Particule détendue ou compressée adiabatiquement sèche de dp hPa
        Durant cette transformation, sa tempréture potentielle et son rapport de mélange
        sont conservés. """
        Ra  = 287.  # constante spécifique gaz parfait air sec (J/kg/°K)
        Cpa = 1005. # chaleur massique à pression constante air sec (J/kg/°K)
        gama=Ra/Cpa
        p_new=self.pression+dp  # évolution de la pression
        t_new=(self.temperature+273.15)*((p_new/self.pression)**gama )# ajustement de la température
        t_new=t_new-273.15
        tVap_new=tVap(p_new,self.rapportDeMelange())# ajustement de la tension de vapeur saturante calcul du nouveau Td
        pointDeRosee_new = tempe(tVap_new) # ajustement de Td
        # print p_new,t_new,tVap_new,pointDeRosee_new
        part_new = Particule (p_new,t_new,pointDeRosee_new)
        return part_new
    def tensionDeVapeur(self):
        return ew(self.temperaturePointDeRosee)
    def tensionDeVapeurSaturante(self):
        return ew(self.temperature)
    def humiditeRelative(self):
        return 100*self.tensionDeVapeur()/self.tensionDeVapeurSaturante()
    def rapportDeMelange(self):
        return rapDeMelange(self.pression,self.tensionDeVapeur())
    def rapportDeMelangeSaturant(self):
        return rapDeMelange(self.pression,self.tensionDeVapeurSaturante())
    def isSaturee(self):
        return (self.temperaturePointDeRosee>=self.temperature)
    def temperaturePotentielle(self):
        return teta(self.pression,self.temperature)
    def ecartTTd(self,pressionDetendue):
        """ calcul de la température du point de rosée apres détente ou compression """
        dp = -(self.pression-pressionDetendue)
        particuleDetendue=self.transfAdiabSeche(dp)
        return particuleDetendue.temperature-particuleDetendue.temperaturePointDeRosee
    def pressionDeCondensation (self):
        """ calcul de la pression de condensation Pc
        en cherchant par la methode de bissection la solution de l'équation
        T(Pc)-Td(Pc) = 0 dans l'interval [10. hPa,self.pression]  """
        return bissection(self.ecartTTd,100.,self.pression)
    def particuleSaturee(self):
        pc= self.pressionDeCondensation()
        part = self.transfAdiabSeche(pc-self.pression)
        t=(part.temperature+part.temperaturePointDeRosee)/2.
        return Particule(pc,t,t)
    def TwZero(self,Tw): # à debugger
        L=2500.
        Cp=1005.
        Pa=2.53*10**15
        Tb=5.42*10**3
        ret= Tw+L/Cp*(0.622*Pa/self.pression*math.exp(-Tb/Tw)-self.rapportDeMelange())
        return ret

    def affiche (self): # affichage des paramètres de la particule
        print "*********************"
        print "donnee pression : ",self.pression," hPa"
        print "donnee temperature : ",self.temperature,"C"
        print "donnee temperature du point de rosee: ",self.temperaturePointDeRosee,"C"
        print "  calculee temperature potentielle: ",self.temperaturePotentielle(),"C"
        print "  calculee saturee: ",self.isSaturee()," (booleen)"
        print "  calculee pression de vapeur: ",self.tensionDeVapeur()," hPa"
        print "  calculee pression de vapeur saturante: ",self.tensionDeVapeurSaturante()," hPa"
        print "  calculee humidite relative: ",self.humiditeRelative()," %"
        print "  calculee rapport de melange : ",self.rapportDeMelange()," g/kg"
        print "  calculee rapport de melange saturant: ",self.rapportDeMelangeSaturant()," g/kg"
        print "*********************"
particule=Particule(700,5.,-6.)  # voir Triplet et Roche page 72
particule.affiche()
particule.particuleSaturee().affiche()
print particule.TwZero(0.)

particule=Particule(850,10,-10)  # voir S. Malardel 2eme édition page 215
particule.affiche()
particule.particuleSaturee().affiche()


