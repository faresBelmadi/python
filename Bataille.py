import Joueur
import Bateau

class BatailleNavale:

    def __init__(self, socket, estClient, dessin):
        self.joueur=[]
        self.socket=socket
        self.client = estClient
        self.caseVisee=()
        self.dessin=dessin
        
    def jouerUnTour(self):
        if self.client == False:
            self.joueur.notifierVisee(self.caseVisee)
            self.socket.sendVisee(self.caseVisee)
            print(self.caseVisee)
            aTouche=self.socket.receivRetour()
            print(aTouche)
            if aTouche:
                self.joueurs[0].notifierTouchee(self.caseVisee)
                self.dessin.dessinToucher()
            toucheVisee= self.socket.receivVisee()
            print(toucheVisee)
            self.socket.sendRetour(self.joueur.estTouche(self.caseVisee))
        else:            
            toucheVisee= self.socket.receivVisee()
            print(toucheVisee)
            self.socket.sendRetour(self.joueur.estTouche(toucheVisee))
            while(self.joueur.aTire == False):
                self.joueur.notifierVisee(self.caseVisee)
                self.socket.sendVisee(self.caseVisee)
                aTouche=self.socket.receivRetour()
                print(aTouche)
                if aTouche:
                    self.joueurs[0].notifierTouchee(self.caseVisee)
            self.jouerUnTour()
