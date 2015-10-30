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


root= Tk()


class grilleInit:


    def __init__(self):
        self.terrain = Canvas(root,width=1140,height=600, bg="white")
        self.terrain.pack()


        for i in range(40,590,50):
            self.terrain.create_line(i,10,i,510)
        for j in range(10,560,50) :
            self.terrain.create_line(40,j,540,j)

        for i in range(590,1140,50):
            self.terrain.create_line(i,10,i,510)
        for j in range(10,560,50) :
            self.terrain.create_line(590,j,1090,j)

        self.alpha = 65
        for i in range(25,515,50):
            self.labelTerrain = Label(self.terrain,text=chr(self.alpha),bg="white")
            self.labelTerrain.place(x=20,y=i)
            self.labelVisee = Label(self.terrain,text=chr(self.alpha),bg="white")
            self.labelVisee.place(x=570,y=i)
            self.alpha += 1

        self.numero=1

        for j in range(30,520,50):

            self.labelTerrain = Label(self.terrain,text=str(self.numero),bg="white")
            self.labelTerrain.place(x=j+35,y=515)
            self.labelVisee = Label(self.terrain,text=str(self.numero),bg="white")
            self.labelVisee.place(x=j+585,y=515)
            self.numero+=1


        self.labelTerrainName = Label(self.terrain,text="Terrain",bg="red")
        self.labelTerrainName.place(x=275,y=550)
        self.labelViseeName = Label(self.terrain,text="Visee",bg="green")
        self.labelViseeName.place(x=825,y=550)

    def GetTerrain(self):
        return self.terrain

    def setTouchee(self, case):
        self.case[case[0]][case[1]]= 2
        return

    def setVisee(self,case):
        self.case[case[0]][case[1]]= 1
        return


