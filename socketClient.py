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

class socketClient(socketBN.socketBN):

    def __init__(self,addresseDistante,portDistant):
        try:
            socketBN.socketBN.__init__(self)
            self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connexion.connect((addresseDistante, portDistant))
            print("je suis conecte chez l'hote")
        except ValueError:
            print ("Erreur connexion")



