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
            joueurCourant.notifierToucher(caseVisee)
        joueurEnnemi.notifierCaseTouchee(caseVisee)
        #modifier graphique
        self.indiceJoueurCourant=1-self.indiceJoueurCourant
        self.jouer()

torpilleur = Bateau.Bateau(2)
contre_torpilleur = Bateau.Bateau(3)
croiseur = Bateau.Bateau(4)
sous_marin = Bateau.Bateau(3)
porte_avion = Bateau.Bateau(5)

bateaux=[torpilleur,contre_torpilleur,croiseur,sous_marin,porte_avion]

roger = Joueur.Joueur("roger",bateaux)
bob = Joueur.Joueur("bob",bateaux)

print(roger.pseudo)
print(torpilleur.taille)

jeu = BatailleNavale([roger,bob])
jeu.jouer()
