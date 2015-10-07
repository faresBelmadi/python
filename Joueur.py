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
                              [0,0,0,0,0,0,0,0,0,0]]
        
        self.grilleVisee = [[0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0]]

    def AjoutBateau(self,bateauInit):
        self.bateaux.append(bateauInit)
        for bateau in self.bateaux:
            for position in bateau.positions:
                #Ajout des positins des bateaux dans la grille du joueur
                self.grilleBateaux[position[0]][position[1]]=3
    
    def notifierTouchee(self,caseVisee):
        self.grilleVisee[caseVisee[0]][caseVisee[1]]= 2
        return

    def estTouche(self, caseVisee):
        for bateau in self.bateaux:
            if bateau.contient(caseVisee):
                self.touche = True
            else:
                self.touche = False
        return self.touche
