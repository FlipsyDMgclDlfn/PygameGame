from tkinter import *

canvas_width = 800
canvas_height = 600

class DrawBox(Frame):
    
    def __init__(self,master):
        master.title( "Draw Box" )
        self.w = Canvas(master, width=canvas_width, height=canvas_height)
        self.w.pack(expand = YES, fill = BOTH)
        self.w.create_rectangle(0,0,canvas_width+1,canvas_height+1,fill="white")
        self.w.bind( "<Button-1>", self.start)
        self.w.bind( "<B1-Motion>", self.draw )
        self.w.bind( "<Button-3>", self.pick)
        self.w.bind("<ButtonRelease-1>",self.stop)
        self.fill = 0
        self.click = False
        self.color = ""
    def start(self,event):
        self.click = True
        self.w.create_rectangle(0,0,canvas_width+1,canvas_height+1,fill="white")
        self.x1 = event.x
        self.y1 = event.y
    def draw( self,event ):
        while (self.click):
            self.w.create_rectangle(0,0,canvas_width+1,canvas_height+1,fill="white")
            self.x2, self.y2 = (event.x + 1), (event.y + 1)
            if self.fill == 0:
                self.w.create_rectangle(self.x1, self.y1, self.x2, self.y2)
            else:
                self.w.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
            self.w.update()
    def stop(self,event):
        self.click = False
    def confirm(self,fill, color):
        self.fill = fill.get()
        self.color = color
    def pick(self,event):
        fill = IntVar()
        color = StringVar()
        color = "black"
        self.chk = Checkbutton(master,text="Fill?",variable=fill, offvalue = 0, onvalue = 1)
        self.chk.pack()
        color = Entry(master)
        color.insert(10, "black")
        color.pack()
        self.confirmB = Button(master, text="Confirm",command=lambda:self.confirm(fill, color.get()))
        self.confirmB.pack()

master = Tk()
draw = DrawBox(master)
    
mainloop()

