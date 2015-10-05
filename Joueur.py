import Bateau

class Joueur:

    def __init__(self,pseudo,bateaux):
        self.pseudo=pseudo
        self.grilleTerrain=[[]]
        self.grilleVisee=[[]]
        self.bateaux= bateaux

    def viserUneCase(self):
        case=input("choisir une case")
        colonne=ord(case[0])
        print(colonne)
        return caseVisee

    def notifierToucher(self,caseVisee):
        #modifier self.grilleVisee
        print("j'ai touché")
        return

    def estTouche(self, caseVisee):
        print("je vérifie si j'ai un bateau sur la case")
        return True

    def notifierCaseTouchee(self,caseVisee):
        print("j'ai été touché sur  "+caseVisee)
        return
