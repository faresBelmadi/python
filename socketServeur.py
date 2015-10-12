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
import socketBN

class socketServeur(socketBN.socketBN):

    def __init__(self,portEcoute):
        try:
            socketBN.socketBN.__init__(self)
            socketServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socketServeur.bind(('', portEcoute))
            socketServeur.listen(1)
            print("j'ecoute")
            self.connexion, infos = socketServeur.accept()
            print("j'ai un joueur")
        except ValueError:
            print ("Erreur connexion")


