import Bateau
import grille


class Joueur:

    def __init__(self,pseudo):
        self.pseudo=pseudo
        self.bateaux = [5]

        self.doitTirer = False
        self.aTirer = False

    def ajoutBateaux(self,bateauxInit):
        self.bateaux = bateauxInit

    #On indique la case visee par le joueur comme vis??e (rouge sur la grille visee)
    def notifierVisee(self,caseVisee):
        self.aTire=True

    def estTouche(self, caseVisee):
        case = (caseVisee['x'],caseVisee['y'])
        for bateau in self.bateaux:
            if bateau.estTouche(case):
                return True
        return False
