import Joueur
import Bateau

class BatailleNavale:

    def __init__(self,joueur, socket, estClient, dessin):
        self.joueur=joueur
        self.socket=socket
        self.client = estClient
        self.caseVisee=()
        self.dessin=dessin
        #Notre compteur nb touchee
        self.nbTouchee=0
        #Compteur nb touchee adversaire
        self.nbToucheeAdverse=0
        #Le serveur commence
        if not estClient:
            self.joueur.doitTirer= True

    def jouerUnTour(self):
        if self.client == False:
            if self.joueur.doitTirer == True and self.joueur.aTirer == True:
                self.joueur.notifierVisee(self.caseVisee)
                self.socket.sendVisee(self.caseVisee)
                aTouche=self.socket.receivRetour()

                if aTouche:
                    self.dessin.dessinToucher()
                    self.nbTouchee+=1
                    if (self.nbTouchee == 17):
                        print("Bravo vous avez gagné")
                else:
                    self.dessin.dessinPasToucher()
                self.joueur.doitTirer=False
                self.joueur.aTirer=False
                self.jouerUnTour()


            if self.joueur.doitTirer == False and self.joueur.aTirer == False:
                self.caseVisee = self.socket.receivVisee()
                aTouche=self.joueur.estTouche(self.caseVisee)
                if aTouche:
                    self.nbToucheeAdverse+=1
                    if (self.nbToucheeAdverse == 17):
                        print("Dommage vous avez perdu")
                self.socket.sendRetour(aTouche)
                self.joueur.doitTirer = True

        else:

            if self.joueur.doitTirer == False and self.joueur.aTirer == False and self.dessin.phasePlacement == False:
                toucheVisee= self.socket.receivVisee()
                aTouche=self.joueur.estTouche(self.caseVisee)
                if aTouche:
                    self.nbToucheeAdverse+=1
                    if (self.nbToucheeAdverse == 17):
                        print("Dommage vous avez perdu")
                self.socket.sendRetour(aTouche)
                self.joueur.doitTirer = True

            elif self.joueur.doitTirer == True and self.joueur.aTirer == True and self.dessin.phasePlacement == False:
                self.joueur.notifierVisee(self.caseVisee)
                self.socket.sendVisee(self.caseVisee)

                aTouche=self.socket.receivRetour()
                if aTouche:
                    self.dessin.dessinToucher()
                    self.nbTouchee+=1
                    if (self.nbTouchee == 17):
                        print("Bravo vous avez gagné")
                else:
                    self.dessin.dessinPasToucher()
                self.joueur.aTirer=False
                self.joueur.doitTirer=False
                self.jouerUnTour()
