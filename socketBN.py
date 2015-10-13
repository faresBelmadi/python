#-------------------------------------------------------------------------------
# Name:        B3-bataillenavale
# Purpose:     Python bataille navale B3
# Version:     PyScripter Portable v2.5.3 x86
#
# Author:      Fares BELMADI, Antoine Lacoste
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*

import socket
import json

class socketBN():

    def __init__(self):
        self.connexion=""
        
    def sendVisee(self,case):
        try:
            chCase=json.dumps(case)
            print("Case envoyée  : "+chCase)
            #print("chCase encodé : "+chCase.encode())
            self.connexion.send(chCase.encode())
        except ValueError:
            print ("Erreur d'envoi")


    def sendRetour(self,chaine):
        try:
            if chaine:
                ch = "1"
            else:
                ch="0"
            self.connexion.send(ch.encode())
        except ValueError:
            print ("Erreur d'envoi")


    def receivVisee(self):
        try:
            self.chRecept = self.connexion.recv(255).decode()

        except ValueError:
            print ("Erreur de reception")
        valeurVisee=json.loads(self.chRecept)
        print("Case reçue : "+valeurVisee)
        return valeurVisee
    
    def receivRetour(self):
        try:
            self.chRecept = self.connexion.recv(255).decode()
            if (self.chRecept=="1"):
                retour = True
            else:
                retour = False
        except ValueError:
            print ("Erreur de reception")

        print("a touché : "+retour)
        return retour

    def __del__(self):
        self.connexion.close()