import Joueur
import Bateau

class BatailleNavale:

    def __init__(self,joueur, socket, estClient, dessin):
        self.joueur=joueur
        self.socket=socket
        self.client = estClient
        self.caseVisee=()
        self.dessin=dessin
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
                    self.joueur.notifierTouchee(self.caseVisee)
                    self.dessin.dessinToucher()
                else:
                    self.dessin.dessinPasToucher()
                self.joueur.doitTirer=False
                self.joueur.aTirer=False
                self.jouerUnTour()


            if self.joueur.doitTirer == False and self.joueur.aTirer == False:
                self.caseVisee = self.socket.receivVisee()
                self.socket.sendRetour(self.joueur.estTouche(self.caseVisee))
                self.joueur.doitTirer = True

        else:
            if self.joueur.doitTirer == False and self.dessin.phasePlacement == False:
                self.caseVisee= self.socket.receivVisee()
                self.socket.sendRetour(self.joueur.estTouche(self.caseVisee))
                self.dessin.dessinOpponent(self.caseVisee)
                self.joueur.doitTirer = True

            elif self.joueur.doitTirer == True and self.joueur.aTirer == True and self.dessin.phasePlacement == False:
                self.joueur.notifierVisee(self.caseVisee)
                self.socket.sendVisee(self.caseVisee)

                aTouche=self.socket.receivRetour()
                if aTouche:
                    self.joueur.notifierTouchee(self.caseVisee)                    
                    self.dessin.dessinToucher()
                else:
                    self.dessin.dessinPasToucher()
                self.joueur.aTirer=False
                self.joueur.doitTirer=False
                self.jouerUnTour()
