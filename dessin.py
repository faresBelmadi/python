#-------------------------------------------------------------------------------
# Name:        B3-bataillenavale
# Purpose:     Python bataille navale B3
# Version:     PyScripter Portable v2.5.3 x86
#
# Author:      Fares BELMADI, Antoine Lacoste
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*

import Bateau

class Dessin:

    def __init__(self):
        self.nombreBateau = 0
        self.phasePlacement = True
        self.alpha = 65
        self.positionsBateaux=[]

    def SetCoord(self,xinit,yinit):
        self.y = yinit
        self.x = xinit

    def GetCoord(self):
        pos = { 'x' : self.CaseX,
                'y' : self.CaseY }
        return pos

    def getPositionsBateaux(self):
        return self.positionsBateaux
    
    def GetTerrain(self,terraininit):
        self.terrain = terraininit

    def dessinBateau(self):
        for i in range(40,540,50):
            if i +50 > self.x > i:# si la coordonnee x est comprise entre i et i+50
                for j in range(10,510,50) :
                        if j+50 > self.y > j:
                            if self.nombreBateau == 0:
                                if j <= 307:
                                    position = []
                                    self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                    pos=(round(i/50),round(j/50))
                                    position.append(pos)
                                    self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                    pos=(round(i/50),round(j/50+1))
                                    position.append(pos)
                                    self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")
                                    pos=(round(i/50),round(j/50+2))
                                    position.append(pos)
                                    self.terrain.create_rectangle(i,j+(50*3),i+50,j+(50*4),fill="blue")
                                    pos=(round(i/50),round(j/50+3))
                                    position.append(pos)
                                    self.terrain.create_rectangle(i,j+(50*4),i+50,j+(50*5),fill="blue")
                                    pos=(round(i/50),round(j/50+4))
                                    position.append(pos)
                                    print(position)
                                    self.positionsBateaux.append(Bateau.Bateau(position))
                                    self.nombreBateau +=1

                            elif self.nombreBateau == 1:
                                if j <= 357:
                                    position = []
                                    self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                    pos=(round(i/50),round(j/50))
                                    if self.estSuperpose(pos) == False:
                                            position.append(pos)
                                            self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                            pos=(round(i/50),round(j/50+1))
                                            position.append(pos)
                                            self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")
                                            pos=(round(i/50),round(j/50+2))
                                            position.append(pos)
                                            self.terrain.create_rectangle(i,j+(50*3),i+50,j+(50*4),fill="blue")
                                            pos=(round(i/50),round(j/50+3))
                                            position.append(pos)
                                            print(position)
                                            self.positionsBateaux.append(Bateau.Bateau(position))
                                            self.nombreBateau +=1

                            elif self.nombreBateau == 2:
                                if j <= 407:
                                    position = []
                                    self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                    pos=(round(i/50),round(j/50))
                                    if self.estSuperpose(pos) == False:
                                        position.append(pos)
                                        self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                        pos=(round(i/50),round(j/50+1))
                                        position.append(pos)
                                        self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")
                                        pos=(round(i/50),round(j/50+2))
                                        position.append(pos)
                                        print(position)
                                        self.positionsBateaux.append(Bateau.Bateau(position))
                                        self.nombreBateau +=1

                            elif self.nombreBateau == 3:
                                if j <= 407:
                                    position = []
                                    self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                    pos=(round(i/50),round(j/50))
                                    if self.estSuperpose(pos) == False:
                                        position.append(pos)
                                        self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                        pos=(round(i/50),round(j/50+1))
                                        position.append(pos)
                                        self.terrain.create_rectangle(i,j+(50*2),i+50,j+(50*3),fill="blue")
                                        pos=(round(i/50),round(j/50+2))
                                        position.append(pos)
                                        print(position)
                                        self.positionsBateaux.append(Bateau.Bateau(position))
                                        self.nombreBateau +=1

                            elif self.nombreBateau == 4:
                                if j <= 457:
                                    position = []
                                    self.terrain.create_rectangle(i,j,i+50,j+50,fill="blue")
                                    pos=(round(i/50),round(j/50))
                                    if self.estSuperpose(pos) == False:
                                        position.append(pos)
                                        self.terrain.create_rectangle(i,j+50,i+50,j+(50*2),fill="blue")
                                        pos=(round(i/50),round(j/50+1))
                                        position.append(pos)
                                        self.positionsBateaux.append(Bateau.Bateau(position))
                                        self.nombreBateau +=1
                                        self.phasePlacement = False


    def dessinVisee(self):
        for i in range(590,1090,50):
            if i +50 > self.x > i:# si la coordonnee x est comprise entre i et i+50
                for j in range(10,510,50) :
                        if j+50 > self.y > j:
                            self.CaseX = round((i-540)/50)
                            self.CaseY = round(j/50)
                            print (str(self.CaseX) + ", " + chr(self.CaseY+self.alpha))
                            self.terrain.create_oval(i,j,i+50,j+50,fill="red")

    def dessinToucher(self):
        for i in range(590,1090,50):
            if i +50 > self.x > i:# si la coordonnee x est comprise entre i et i+50
                for j in range(10,510,50) :
                        if j+50 > self.y > j:
                            self.terrain.create_oval(i,j,i+50,j+50,fill="black")

    def estSuperpose(self,pos):
        for bateau in self.positionsBateaux:
            for position in bateau.positions:
                if pos == position:
                    return True
        return False
