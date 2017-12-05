from tkinter import *
import time
import random

class Hanoi(Frame):
    def __init__(self, master):
        self.tower1 = []
        self.tower2 = []
        self.tower3 = []
        disks = int(input("How many disks? "))
        for i in range(0,disks):
            self.tower1 += [disks - i]
        self.width = 3*(10 + (disks * 10)) + 10
        self.height = 12 * disks
        self.towers = Canvas(master, width = self.width, height = self.height)
        self.towers.pack()
        self.moveTower(disks,1,3,2)
    def getTower(self,t):
        if t == 1:
            return self.tower1
        elif t == 2:
            return self.tower2
        else:
            return self.tower3
        
    def moveTower(self,x,s,d,e):
        if x >= 1:
            self.moveTower(x-1,s,e,d)
            self.moveDisk(s,d)
            self.moveTower(x-1,e,d,s)
    def createDisk(self,x,d,t):
        y = random.randint(-1,6)
        if y == 0:
            color = "red"
        elif y == 1:
            color = "orange"
        elif y == 2:
            color = "yellow"
        elif y == 3:
            color = "green"
        elif y == 4:
            color = "blue"
        elif y == 5:
            color = "purple"
        else:
            color = "pink"
        if t == 1:
            self.towers.create_rectangle(self.width/6-(5*x), self.height-(2*(d-1) + 10*d),(self.width/6)+(5*x), self.height-(2*(d-1) + 10*(d-1)),fill=color)
        if t == 2:
            self.towers.create_rectangle((self.width/2)-(5*x), self.height-(2*(d-1) + 10*d),(self.width/2)+(5*x), self.height-(2*(d-1) + 10*(d-1)),fill=color)
        if t == 3:
            self.towers.create_rectangle((5*self.width/6)-(5*x), self.height-(2*(d-1) + 10*d),(5*self.width/6)+(5*x), self.height-(2*(d-1) + 10*(d-1)),fill=color)
    def moveDisk(self,fp,tp):
        d1 = 1
        d2 = 1
        d3 = 1
        y = random.randint(-1,6)
        if y == 0:
            color = "red"
        elif y == 1:
            color = "orange"
        elif y == 2:
            color = "yellow"
        elif y == 3:
            color = "green"
        elif y == 4:
            color = "blue"
        elif y == 5:
            color = "purple"
        else:
            color = "pink"
        self.towers.create_rectangle(0,0,self.width,self.height,fill=color)
        y = random.randint(-1,6)
        if y == 0:
            color = "red"
        elif y == 1:
            color = "orange"
        elif y == 2:
            color = "yellow"
        elif y == 3:
            color = "green"
        elif y == 4:
            color = "blue"
        elif y == 5:
            color = "purple"
        else:
            color = "pink"
        self.towers.create_rectangle(self.width/6 - 2, 0, self.width/6 + 2, self.height, fill=color)
        y = random.randint(-1,6)
        if y == 0:
            color = "red"
        elif y == 1:
            color = "orange"
        elif y == 2:
            color = "yellow"
        elif y == 3:
            color = "green"
        elif y == 4:
            color = "blue"
        elif y == 5:
            color = "purple"
        else:
            color = "pink"
        self.towers.create_rectangle(self.width/2 - 2, 0, self.width/2 + 2, self.height, fill=color)
        y = random.randint(-1,6)
        if y == 0:
            color = "red"
        elif y == 1:
            color = "orange"
        elif y == 2:
            color = "yellow"
        elif y == 3:
            color = "green"
        elif y == 4:
            color = "blue"
        elif y == 5:
            color = "purple"
        else:
            color = "pink"
        self.towers.create_rectangle(5*self.width/6 - 2, 0, 5*self.width/6 + 2, self.height, fill=color)
        for disks in self.tower1:
            self.createDisk(disks,d1,1)
            d1 += 1
        for disks in self.tower2:
            self.createDisk(disks,d2,2)
            d2 += 1
        for disks in self.tower3:
            self.createDisk(disks,d3,3)
            d3 += 1
        self.towers.pack()
        self.towers.after(0)
        self.towers.update()
        a = self.getTower(tp)
        b = self.getTower(fp)
        a += [b[len(b) - 1]]
        del self.getTower(fp)[len(self.getTower(fp)) - 1]
        print("moving disk from",fp,"to",tp)
        if (len(self.tower1) == 0 and len(self.tower2) == 0):
            d1 = 1
            d2 = 1
            d3 = 1
            self.towers.create_rectangle(0,0,self.width,self.height,fill="white")
            self.towers.create_rectangle(self.width/6 - 2, 0, self.width/6 + 2, self.height, fill="black")
            self.towers.create_rectangle(self.width/2 - 2, 0, self.width/2 + 2, self.height, fill="black")
            self.towers.create_rectangle(5*self.width/6 - 2, 0, 5*self.width/6 + 2, self.height, fill="black")
            for disks in self.tower1:
                self.createDisk(disks,d1,1)
                d1 += 1
            for disks in self.tower2:
                self.createDisk(disks,d2,2)
                d2 += 1
            for disks in self.tower3:
                self.createDisk(disks,d3,3)
                d3 += 1
            self.towers.pack()
            self.towers.after(50)
            self.towers.update()            
    
root = Tk()
hanoi = Hanoi(root)
root.mainloop()
