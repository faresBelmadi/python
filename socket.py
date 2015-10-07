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

socket.sockets

class socketClient():


    def __init__(self,addresseDistante,portDistant):
        try:

            self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketClient.connect((addresseDistante, portDistant))
        except ValueError:
            print "Erreur connexion"



    def sendVise(self,case):

        try:
            chCase = str(case[0])+str(case[1])
            self.socketClient.send(chCase)
        except ValueError:
            print "Erreur d'envoi"


    def receiv(self):

        try:
            self.chRecept = self.socketClient.recv(255)

        except ValueError:
            print "Erreur de reception"

        return self.chRecept

    def __del__(self):
        self.socketClient.close()

class socketServeur():

    def __init__(self,portEcoute):
        try:

            self.socketServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketServeur.bind(('', portEcoute))
            self.socketServeur.accept()
            self.socketServeur.listen(1)
            break
        except ValueError:
            print "Erreur connexion"


    def sendVise(self,case):

        try:
            chCase = str(case[0])+str(case[1])
            self.socketServeur.send(chCase)
        except ValueError:
            print "Erreur d'envoi"


    def receiv(self):

        try:
            self.chRecept = self.socketServeur.recv(255)

        except ValueError:
            print "Erreur de reception"

        return self.chRecept
    def __del__(self):
        self.socketServeur.close()

