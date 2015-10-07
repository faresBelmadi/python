import Joueur
import Bateau

class BatailleNavale:

    def __init__(self,joueurs):
        self.joueurs=joueurs
        self.indiceJoueurCourant=0

    def jouerUnTour(self, caseVisee):
        joueurCourant=self.joueurs[self.indiceJoueurCourant]
        joueurEnnemi=self.joueurs[1-self.indiceJoueurCourant]
        aTouche = joueurEnnemi.estTouche(caseVisee)
        if aTouche:
            joueurCourant.notifierTouchee(caseVisee)
            joueurEnnemi.notifierCaseTouchee(caseVisee)
        self.indiceJoueurCourant=1-self.indiceJoueurCourant
