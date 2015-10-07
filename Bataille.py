import Joueur
import Bateau

class BatailleNavale:

    def __init__(self, socket, estClient):
        self.joueur=[]
        self.socket=socket
        self.client = estClient
        self.caseVisee=()
        
    def jouerUnTour(self):
        if self.client == False:
            self.joueur.notifierVisee(self.caseVisee)
            socket.sendVise(self.caseVisee)
            aTouche=socket.receiv()
            if aTouche:
                self.joueurs[0].notifierTouchee(self.caseVisee)
            toucheVisee= socket.receiv()
            self.socket.send(self.joueur.estTouche(self.caseVisee))
        else:            
            toucheVisee= socket.receiv()
            self.socket.send(self.joueur.estTouche(self.caseVisee))
            while(self.joueur.aTire == False):
                self.joueur.notifierVisee(self.caseVisee)
                socket.sendVise(self.caseVisee)
                aTouche=socket.receiv()
                if aTouche:
                    self.joueurs[0].notifierTouchee(self.caseVisee)
            self.jouerUnTour()
