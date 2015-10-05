#-------------------------------------------------------------------------------
# Name:        B3-bataillenavale
# Purpose:     Python bataille navale B3
# Version:     PyScripter Portable v2.5.3 x86
#
# Author:      Fares BELMADI
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*


class Event:
    global ClickX,ClickY,Clicked
    ClickX = 0
    ClickY = 0
    Clicked = False

    def reportEventClick(self,event):
        ClickX = event.x
        ClickY = event.y

        if 540 > ClickX > 40:
            if 510 > ClickY > 10:
                print (str(ClickX) + ", " + str(ClickY))
                Clicked = True


    def GetX(self):

        return ClickX

    def GetY(self):
        return ClickY

    def Click(self):
        return Clicked