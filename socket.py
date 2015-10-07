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
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect((addresseDistante, portDistant))





class socketServeur():

    def __init__(self,portEcoute):
        self.socketServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketServeur.bind(('', portEcoute))