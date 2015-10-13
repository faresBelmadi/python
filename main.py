#-------------------------------------------------------------------------------
# Name:        B3-bataillenavale
# Purpose:     Python bataille navale B3
# Version:     PyScripter Portable v2.5.3 x86
#
# Author:      Fares BELMADI, Antoine Lacoste
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys

if (sys.version_info > (3, 0)):
     # Python 3 code in this block
    from tkinter import *
else:
     # Python 2 code in this block
    from Tkinter import *


import event
import grille
import dessin
import Joueur
import Bataille
import socketClient
import socketServeur


"""
    2 joueurs
    5 bateaux
            1 porte avion 5 cases
            1 croiseurs 4 cases
            1 sous marin 3 cases
            1 contre torpilleur 3
            1 torpilleur 2

    taille:
            10x10
            1->10
            A->J

    d?buts:
            demande de pseudo a chaque joueur
            premier a jouer : random


    placement
            chaque joueur place les batiments

    jeu
            jouer1 puis joueur2

    fin
            tous les batiments sont coul?es
"""

def reportEventClick(event):
        ClickX = event.x
        ClickY = event.y
        print (str(ClickX) + ", " + str(ClickY))
        dessinBateau.SetCoord(ClickX,ClickY)

        if dessinBateau.phasePlacement == True:
            if 540 > ClickX > 40:
                if 510 > ClickY > 10:
                    dessinBateau.dessinBateau()

        else:
            roger.ajoutBateaux(dessinBateau.getPositionsBateaux())
            if 1090 > ClickX > 590:
                if 510 > ClickY > 10:
                    dessinBateau.dessinVisee()
                    jeu.caseVisee=dessinBateau.GetCoord()
                    jeu.jouerUnTour()


init = grille.grilleInit()
eventClick = event.Event()
dessinBateau = dessin.Dessin()

text = Text(init.terrain)
#text.insert("Entrer un pseudo")

roger = Joueur.Joueur("roger")
socket = socketClient.socketClient("10.69.0.156",60155)
#socket = socketServeur.socketServeur(60155)
#socket.sendVisee((2,3))
#print(socket.receiv())
jeu = Bataille.BatailleNavale(socket,False,dessinBateau)

dessinBateau.GetTerrain(init.GetTerrain())

init.terrain.bind("<Button-1>",reportEventClick)
init.terrain.pack()

grille.root.mainloop()

