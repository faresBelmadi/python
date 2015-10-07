#-------------------------------------------------------------------------------
# Name:        B3-bataillenavale
# Purpose:     Python bataille navale B3
# Version:     PyScripter Portable v2.5.3 x86
#
# Author:      Fares BELMADI
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*

import socket

class socketClient():


    def __init__(self,addresseDistante,portDistant):
        try:

            self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketClient.connect((addresseDistante, portDistant))
        except ValueError:
            print ("Erreur connexion")



    def sendVise(self,case):

        try:
            chCase = str(case[0])+str(case[1])
            self.socketClient.send(b'coucou')
        except ValueError:
            print ("Erreur d'envoi")

    def sendRetour(self,chaine):

        try:
            self.socketClient.send(chaine)
        except ValueError:
            print ("Erreur d'envoi")


    def receiv(self):

        try:
            self.chRecept = self.socketClient.recv(255)

        except ValueError:
            print ("Erreur de reception")

        return self.chRecept

    def __del__(self):
        self.socketClient.close()

class socketServeur():

    def __init__(self,portEcoute):
        try:

            self.socketServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketServeur.bind(('', portEcoute))
            self.socketServeur.listen(1)
            print("jécoute")
            self.connexClient, infos = self.socketServeur.accept()
            print("jai un joueur")
        except ValueError:
            print ("Erreur connexion")


    def sendVise(self,case):

        try:
            chCase = str(case[0])+str(case[1])
            self.connexClient.send(chCase)
        except ValueError:
            print ("Erreur d'envoi")

    def sendRetour(self,chaine):

        try:
            self.connexClient.send(chaine)
        except ValueError:
            print ("Erreur d'envoi")


    def receiv(self):

        try:
            self.chRecept = self.connexClient.recv(255)

        except ValueError:
            print ("Erreur de reception")

        return self.chRecept
    
    def __del__(self):
        self.socketServeur.close()

