from tkinter import *
from collections import Counter
import random
from tkinter.ttk import *
import time
class MatchGame():    
    
    def __init__(self):
        self.turns = 0
        self.matches = 0
        self.buttons = []
        self.a = 0
        self.match1 = 0
        self.match2 = 0
        self.match1Button = 0
        self.match2Button = 0
        self.wasMatch = False
        master.title((str(self.matches),"matches"))
        k = 0
        temp = 0
        self.r = []
        while len(self.r) < 52:
            temp = random.randint(1,26)
            if self.r.count(temp) < 2:
                self.r += [temp]
        for i in range(0,4):
            for j in range(0,13):
                self.makeButton(k,i,j)
                k += 1
                
    def makeButton(self,num,i,j):
        img = PhotoImage(file="cardback.gif")
        p = Button(master, image=img, command=lambda: self.match(num,i,j))
        ##p.grid(row=i,column=j,padx=0,pady=0)
        ##p.configure(image=img)
        p.grid(row=i,column=j,padx=0,pady=0)
        self.buttons += [p]
        
    def match(self,x,i,j):
        print("Its a", self.r[x],"!")
        if self.a == 0:
            if not self.wasMatch:
                self.buttons[self.match2Button].configure(state=NORMAL)#, text = " ")
                self.buttons[self.match1Button].configure(state=NORMAL)#, text = " ")
            self.wasMatch = False
            self.match1 = self.r[x]
            self.buttons[x].configure(state=DISABLED)#, text = self.r[x])
            self.match1Button = x
            self.match1Buttonx = i
            self.match1Buttony = j
            self.a += 1
        else:
            self.match2 = self.r[x]
            self.buttons[x].configure(state=DISABLED)#, text = self.r[x])
            self.match2Button = x
            self.match2Buttonx = i
            self.match2Buttony = j
            self.testMatch()
            
    def testMatch(self):
        if self.match1 == self.match2:
            print("It's a match")
            self.wasMatch = True
            self.matches += 1
            master.title((str(self.matches),"matches"))
        else:
            print("Not a match, try again!")
            self.turns += 1
        self.a = 0
        self.match1 = 0
        self.match2 = 0
        if self.matches == 26:
            print("You won in",self.turns,"turns!")

master = Tk()
game = MatchGame()
mainloop()










