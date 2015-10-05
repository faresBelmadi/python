#-------------------------------------------------------------------------------
# Name:        B3-bataillenavale
# Purpose:     Python bataille navale B3
# Version:     PyScripter Portable v2.5.3 x86
#
# Author:      Fares BELMADI
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*

from Tkinter import *

import event
import grille
import dessin
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
        dessinBateau.GetCoord(ClickX,ClickY)

        if dessinBateau.phasePlacement == True:
            if 540 > ClickX > 40:
                if 510 > ClickY > 10:
                    dessinBateau.dessinBateau()

        if dessinBateau.phasePlacement == False:
            if 1090 > ClickX > 590:
                if 510 > ClickY > 10:
                    dessinBateau.dessinVisee()



init = grille.grille()
eventClick = event.Event()
dessinBateau = dessin.Dessin()

dessinBateau.GetTerrain(init.GetTerrain())

init.terrain.bind("<Button-1>",reportEventClick)
init.terrain.pack()

grille.root.mainloop()