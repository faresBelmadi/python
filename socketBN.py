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

class socketBN():

    def __init__(self):
        self.connexion=""
        
    def sendVisee(self,case):
        try:
            chCase = str(case[0])+str(case[1])
            self.connexion.send(chCase)
        except ValueError:
            print ("Erreur d'envoi")


    def sendRetour(self,chaine):
        try:
            self.connexion.send(chaine)
        except ValueError:
            print ("Erreur d'envoi")


    def receiv(self):
        try:
            self.chRecept = self.connexion.recv(255)

        except ValueError:
            print ("Erreur de reception")

        return self.chRecept
    
    def __del__(self):
        self.connexion.close()


