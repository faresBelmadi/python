import Joueur
import Bateau

class BatailleNavale:

    def __init__(self,joueur, socket, estClient, dessin):
        self.joueur=joueur
        self.socket=socket
        self.client = estClient
        self.caseVisee=()
        self.dessin=dessin
        if estClient:
            self.jouerUnTour()

    def jouerUnTour(self):
        if self.client == False:
            if self.joueur.doitTirer == True and self.joueur.aTirer == True:
                self.joueur.notifierVisee(self.caseVisee)
                self.socket.sendVisee(self.caseVisee)
                aTouche=self.socket.receivRetour()

                if aTouche:
                    self.joueurs[0].notifierTouchee(self.caseVisee)
                    self.dessin.dessinToucher()


            if self.joueur.doitTirer == False and self.joueur.aTirer == False:
                toucheVisee= self.socket.receivVisee()
                self.socket.sendRetour(self.joueur.estTouche(self.caseVisee))

        else:

            if self.joueur.doitTirer == False:
                toucheVisee= self.socket.receivVisee()
                self.joueur.doitTirer = True

            elif self.joueur.doitTirer == True and self.joueur.aTirer == True:
                self.socket.sendRetour(self.joueur.estTouche(toucheVisee))

                self.joueur.notifierVisee(self.caseVisee)
                self.socket.sendVisee(self.caseVisee)

                aTouche=self.socket.receivRetour()
                if aTouche:
                    self.joueurs[0].notifierTouchee(self.caseVisee)


