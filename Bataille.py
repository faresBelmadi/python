import Joueur
import Bateau

class BatailleNavale:

    def __init__(self,joueurs):
        self.joueurs=joueurs
        self.indiceJoueurCourant=0
        
    def jouer(self):
        joueurCourant=self.joueurs[self.indiceJoueurCourant]
        joueurEnnemi=self.joueurs[1-self.indiceJoueurCourant]
        caseVisee=joueurCourant.viserUneCase()
        aTouche = joueurEnnemi.estTouche(caseVisee)
        if aTouche:
            joueurCourant.notifierTouchee(caseVisee)
        joueurEnnemi.notifierCaseTouchee(caseVisee)
        #modifier graphique
        self.indiceJoueurCourant=1-self.indiceJoueurCourant
        self.jouer()

