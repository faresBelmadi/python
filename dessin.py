#-------------------------------------------------------------------------------
# Name:        B3-bataillenavale
# Purpose:     Python bataille navale B3
# Version:     PyScripter Portable v2.5.3 x86
#
# Author:      Fares BELMADI
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*


class Dessin:

    def __init__(self):
        self.nombreBateau = 0
        self.phasePlacement = True

    def GetCoord(self,xinit,yinit):
        self.y = yinit
        self.x = xinit

    def GetTerrain(self,terraininit):
        self.terrain = terraininit

    def dessinBateau(self):
        for i in range(40,540,50):
            if i +50 > self.x > i:# si la coordonnee x est comprise entre i et i+50
                for j in range(10,510,50) :
                        if j+50 > self.y > j:
                            if self.nombreBateau == 0:
                                self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")
                                self.terrain.create_rectangle(i,j+(50*3),i+50,j+(50*4),fill="blue")
                                self.terrain.create_rectangle(i,j+(50*4),i+50,j+(50*5),fill="blue")

                            elif self.nombreBateau == 1:
                                self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")
                                self.terrain.create_rectangle(i,j+(50*3),i+50,j+(50*4),fill="blue")

                            elif self.nombreBateau == 2:
                                self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")

                            elif self.nombreBateau == 3:
                                self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")

                            elif self.nombreBateau == 4:
                                self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                self.phasePlacement = False
        self.nombreBateau +=1


    def dessinVisee(self):

        for i in range(590,1090,50):
            if i +50 > self.x > i:# si la coordonnee x est comprise entre i et i+50
                for j in range(10,510,50) :
                        if j+50 > self.y > j:
                            self.terrain.create_oval(i,j,i+50,j+50,fill="red")