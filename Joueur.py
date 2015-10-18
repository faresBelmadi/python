import Bateau
import grille


class Joueur:

    def __init__(self,pseudo):
        self.pseudo=pseudo
        self.bateaux = [5]
        self.grilleBateaux = [[0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0]]

        self.grilleVisee = [[0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0]]

        self.doitTirer = False
        self.aTirer = False

    def ajoutBateaux(self,bateauxInit):
        self.bateaux = bateauxInit
        for bateau in self.bateaux:
            for position in bateau.positions:
                #Ajout des positions des bateaux dans la grille du joueurs
                self.grilleBateaux[position[0]-1][position[1]-1]=3

    #On indique la case visee par le joueur comme vis??e (rouge sur la grille visee)
    def notifierVisee(self,caseVisee):
        self.grilleVisee[caseVisee['x']][caseVisee['y']]= 1
        self.aTire=True

    #On indique si une case vis??e a touch?? un bateau (case noire sur la grille vis??e)
    def notifierTouchee(self,caseVisee):
        self.grilleVisee[caseVisee['x']][caseVisee['y']]= 2

    def estTouche(self, caseVisee):
        case = (caseVisee['x'],caseVisee['y'])
        for bateau in self.bateaux:
            if bateau.estTouche(case):
                return True
        return False
