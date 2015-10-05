import Bateau

class Joueur:

    def __init__(self,pseudo,bateaux):
        self.pseudo=pseudo
        self.grilleTerrain=Grille()
        self.grilleVisee= Grille()
        self.bateaux= bateaux

    def viserUneCase(self):
        case=input("choisir une case")
        colonne = ord(lower(case[0])-65) 
        ligne = case[1:]
        caseVisee=(ligne,colonne)
        self.grilleVisee.setVisee(caseVIsee)
        return caseVisee

    def notifierTouchee(self,caseVisee):
        self.grilleVisee.setTouchee(caseVisee)
        return

    def estTouche(self, caseVisee):
        for bateau in self.bateaux:
            if bateau.contient(caseVisee):
                return True
        return False

    def notifierCaseTouchee(self,caseVisee):
        self.grilleTerrain.setTouchee(caseVisee)
        return
