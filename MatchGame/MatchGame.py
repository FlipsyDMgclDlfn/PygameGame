from tkinter import *
from collections import Counter
import random
from tkinter.ttk import *
import time
class MatchGame():    
    
    def __init__(self):
        
        self.back = PhotoImage(file="cardback.gif")
        
        self.aos = PhotoImage(file="aos.gif")
        self.twoos = PhotoImage(file="2os.gif")
        self.threeos = PhotoImage(file="3os.gif")
        self.fouros = PhotoImage(file="4os.gif")
        self.fiveos = PhotoImage(file="5os.gif")
        self.sixos = PhotoImage(file="6os.gif")
        self.sevenos = PhotoImage(file="7os.gif")
        self.eightos = PhotoImage(file="8os.gif")
        self.nineos = PhotoImage(file="9os.gif")
        self.tenos = PhotoImage(file="10os.gif")
        self.jos = PhotoImage(file="jos.gif")
        self.qos = PhotoImage(file="qos.gif")
        self.kos = PhotoImage(file="kos.gif")
        
        self.aoh = PhotoImage(file="aoh.gif")
        self.twooh = PhotoImage(file="2oh.gif")
        self.threeoh = PhotoImage(file="3oh.gif")
        self.fouroh = PhotoImage(file="4oh.gif")
        self.fiveoh = PhotoImage(file="5oh.gif")
        self.sixoh = PhotoImage(file="6oh.gif")
        self.sevenoh = PhotoImage(file="7oh.gif")
        self.eightoh = PhotoImage(file="8oh.gif")
        self.nineoh = PhotoImage(file="9oh.gif")
        self.tenoh = PhotoImage(file="10oh.gif")
        self.joh = PhotoImage(file="joh.gif")
        self.qoh = PhotoImage(file="qoh.gif")
        self.koh = PhotoImage(file="koh.gif")
        
        self.turns = 0
        self.matches = 0
        self.buttons = []
        self.a = 0
        self.match1 = 0
        self.match2 = 0
        self.match1Button = 0
        self.match2Button = 0
        self.wasMatch = True
        master.title((str(self.matches)+" matches and "+ str(self.turns)+ " turns!"))
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
        p = Button(master, image=self.back, command=lambda: self.match(num,i,j))
        p.grid(row=i,column=j,padx=0,pady=0)
        self.buttons += [p]
        
    def match(self,x,i,j):
        print("Its a", self.r[x],"!")
        if self.r[x] == 1:
            img = self.aos
        if self.r[x] == 2:
            img = self.twoos
        if self.r[x] == 3:
            img = self.threeos
        if self.r[x] == 4:
            img = self.fouros
        if self.r[x] == 5:
            img = self.fiveos
        if self.r[x] == 6:
            img = self.sixos
        if self.r[x] == 7:
            img = self.sevenos
        if self.r[x] == 8:
            img = self.eightos
        if self.r[x] == 9:
            img = self.nineos
        if self.r[x] == 10:
            img = self.tenos
        if self.r[x] == 11:
            img = self.jos
        if self.r[x] == 12:
            img = self.qos
        if self.r[x] == 13:
            img = self.kos
        if self.r[x] == 14:
            img = self.aoh
        if self.r[x] == 15:
            img = self.twooh
        if self.r[x] == 16:
            img = self.threeoh
        if self.r[x] == 17:
            img = self.fouroh
        if self.r[x] == 18:
            img = self.fiveoh
        if self.r[x] == 19:
            img = self.sixoh
        if self.r[x] == 20:
            img = self.sevenoh
        if self.r[x] == 21:
            img = self.eightoh
        if self.r[x] == 22:
            img = self.nineoh
        if self.r[x] == 23:
            img = self.tenoh
        if self.r[x] == 24:
            img = self.joh
        if self.r[x] == 25:
            img = self.qoh
        if self.r[x] == 26:
            img = self.koh
        if self.a == 0:
            if not self.wasMatch:
                self.buttons[self.match2Button].configure(state=NORMAL,image=self.back)
                self.buttons[self.match1Button].configure(state=NORMAL,image=self.back)
            self.wasMatch = False
            self.match1 = self.r[x]
            self.buttons[x].configure(state=DISABLED,image=img)
            self.match1Button = x
            self.match1Buttonx = i
            self.match1Buttony = j
            self.a += 1
        else:
            self.match2 = self.r[x]
            self.buttons[x].configure(state=DISABLED,image=img)
            self.match2Button = x
            self.match2Buttonx = i
            self.match2Buttony = j
            self.testMatch()
            
    def testMatch(self):
        if self.match1 == self.match2:
            print("It's a match")
            self.wasMatch = True
            self.matches += 1
        else:
            print("Not a match, try again!")
            self.turns += 1
        master.title((str(self.matches)+ " matches and "+ str(self.turns)+ " turns!"))
        self.a = 0
        self.match1 = 0
        self.match2 = 0
        if self.matches == 26:
            print("You won in",self.turns,"turns!")

master = Tk()
game = MatchGame()
mainloop()





















































