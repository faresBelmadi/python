import Bateau
import grille


class Joueur:

    def __init__(self,pseudo):
        self.pseudo=pseudo
        self.bateaux = [5]
        self.caseVise = [100]

    def AjoutBateau(self,bateauInit):
        self.bateaux.append(bateauInit)



#ne concerne pas le Joueur

    def viserUneCase(self):

        return 0
"""
    def notifierTouchee(self,caseVisee):
        self.grilleVisee.setTouchee(caseVisee)
        return

    def estTouche(self, caseVisee):
        for bateau in self.bateaux:
            if bateau.contient(caseVisee):
                self.touche = True
            else:
                self.touche = False
        return self.touche

    def notifierCaseTouchee(self,caseVisee):
        self.grilleTerrain.setTouchee(caseVisee)
        return"""
