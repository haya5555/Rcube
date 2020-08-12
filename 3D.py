from vpython import *
import time
import random

red = vector(255,0,0)
blue = vector(0,0,255)
green = vector(0,255,0)
white = vector(255,255,255)
yellow = vector(255,255,0)
skycolor = vector(0,255,255)
black = vector(0,0,0)

class PartsOfCube:
    def __init__(self, *, pos, axis=vector(0,0,0)):
        self.pos = pos

        posx = self.pos.x
        posy = self.pos.y
        posz = self.pos.z

        self.partsList = [None] * 18
        self.partsList[0] = box(color = red,#天井
        pos = vector(posx+0.5, posy+1, posz+0.5),
        size = vector(1, 0.01, 1),
        axis = axis)
        self.partsList[1] = box(color = blue,#底
        pos = vector(posx+0.5, posy, posz+0.5),
        size = vector(1, 0.01, 1),
        axis = axis)
        self.partsList[2] = box(color = green,#側面1
        pos = vector(posx+0.5, posy+0.5, posz),
        size = vector(1, 1, 0.01),
        axis = axis)
        self.partsList[3] = box(color = white,#側面2
        pos = vector(posx, posy+0.5, posz+0.5),
        size = vector(0.01, 1, 1),
        axis = axis)
        self.partsList[4] = box(color = yellow,#側面3
        pos = vector(posx+1, posy+0.5, posz+0.5),
        size = vector(0.01, 1, 1),
        axis = axis)
        self.partsList[5] = box(color = skycolor,#側面4
        pos = vector(posx+0.5,posy+0.5,posz+1),
        size = vector(1, 1, 0.01),
        axis = axis)

        #辺
        self.partsList[6] = box(color = black,
        pos = vector(posx+0.5,posy,posz),
        size = vector(1, 0.02, 0.02),
        axis = axis)
        self.partsList[7] = box(color = black,
        pos = vector(posx+0.5,posy+1,posz),
        size = vector(1, 0.02, 0.02),
        axis = axis)
        self.partsList[8] = box(color = black,
        pos = vector(posx+0.5,posy,posz+1),
        size = vector(1, 0.02, 0.02),
        axis = axis)
        self.partsList[9] = box(color = black,
        pos = vector(posx+0.5,posy+1,posz+1),
        size = vector(1, 0.02, 0.02),
        axis = axis)
        self.partsList[10] = box(color = black,
        pos = vector(posx,posy+0.5,posz),
        size = vector(0.02, 1, 0.02),
        axis = axis)
        self.partsList[11] = box(color = black,
        pos = vector(posx+1,posy+0.5,posz),
        size = vector(0.02, 1, 0.02),
        axis = axis)
        self.partsList[12] = box(color = black,
        pos = vector(posx,posy+0.5,posz+1),
        size = vector(0.02, 1, 0.02),
        axis = axis)
        self.partsList[13] = box(color = black,
        pos = vector(posx+1,posy+0.5,posz+1),
        size = vector(0.02, 1, 0.02),
        axis = axis)
        self.partsList[14] = box(color = black,
        pos = vector(posx,posy,posz+0.5),
        size = vector(0.02, 0.02, 1),
        axis = axis)
        self.partsList[15] = box(color = black,
        pos = vector(posx+1,posy,posz+0.5),
        size = vector(0.02, 0.02, 1),
        axis = axis)
        self.partsList[16] = box(color = black,
        pos = vector(posx,posy+1,posz+0.5),
        size = vector(0.02, 0.02, 1),
        axis = axis)
        self.partsList[17] = box(color = black,
        pos = vector(posx+1,posy+1,posz+0.5),
        size = vector(0.02, 0.02, 1),
        axis = axis)

        self.parts = compound(self.partsList)

    def rotate(self, *, angle, axis, origin):
        self.parts.rotate(angle=angle,axis=axis,origin=origin)
        self.pos = self.parts.pos - vector(0.5,0.5,0.5)
        self.pos = vector(round(self.pos.x), round(self.pos.y), round(self.pos.z))

class Cube:
    def __init__(self,n):
        self.n = n
        self.partsList = []
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    self.partsList.append(PartsOfCube(pos = vector(x, y, z)))

    def rotateQuickly(self, axis, n):
        if axis == "x":
            for parts in self.partsList:
                if parts.pos.x == n:
                    parts.rotate(angle=pi/2, axis=vector(1, 0, 0), origin=vector(self.n/2,self.n/2,self.n/2))
        elif axis == "y":
            for parts in self.partsList:
                if parts.pos.y == n:
                    parts.rotate(angle=pi/2, axis=vector(0, 1, 0), origin=vector(self.n/2,self.n/2,self.n/2))
        elif axis == "z":
            for parts in self.partsList:
                if parts.pos.z == n:
                    parts.rotate(angle=pi/2, axis=vector(0, 0, 1), origin=vector(self.n/2,self.n/2,self.n/2))

    def collapses(self):
        for i in range(2):
            axis = random.choice(("x", "y", "z"))
            n = random.randint(0, self.n-1)
            self.rotateQuickly(axis, n)

    def rotate(self, axis, n):
        rotatePartses = []
        if axis == "x":
            axis = vector(1, 0, 0)
            for parts in self.partsList:
                if parts.pos.x == n:
                    rotatePartses.append(parts)
        elif axis == "y":
            axis = vector(0, 1, 0)
            for parts in self.partsList:
                if parts.pos.y == n:
                    rotatePartses.append(parts)
        elif axis == "z":
            axis = vector(0, 0, 1)
            for parts in self.partsList:
                if parts.pos.z == n:
                    rotatePartses.append(parts)
        origin = vector(self.n/2,self.n/2,self.n/2)
        for i in range(90):
            for parts in rotatePartses:
                parts.rotate(angle=pi/180, axis=axis, origin=origin)
            time.sleep(0.02)

if __name__ == "__main__":
    cube = Cube(5)
    arrow(color=white, pos=vector(0, 0, 0), axis=vector(7, 0, 0), shaftwidth=0.5)
    arrow(color=white, pos=vector(0, 0, 0), axis=vector(0, 7, 0), shaftwidth=0.5)
    arrow(color=white, pos=vector(0, 0, 0), axis=vector(0, 0, 7), shaftwidth=0.5)
    text(color=white, pos=vector(9, 0, 0), text="x")
    text(color=white, pos=vector(0, 9, 0), text="y")
    text(color=white, pos=vector(0, 0, 9), text="z")

    scene.center = vector(0, 0, 0)
    posOfCamera = vector(3, 3, 3)
    scene.forward = scene.center - posOfCamera

    def movecamera():
        global posOfCamera
        posOfCamera *= -1
        scene.forward = scene.center - posOfCamera

    import tkinter as tk
    root = tk.Tk()
    texts = ("x", "y", "z")
    val = tk.IntVar()
    for i in range(3):
        radiobutton = tk.Radiobutton(root,
        value = i,
        variable = val,
        text = texts[i])
        radiobutton.pack()
    nEntry = tk.Entry(width=1)
    nEntry.pack()
    rotateButton = tk.Button(root,
    text = "rotate",
    command = lambda : cube.rotate(texts[val.get()], int(nEntry.get())))
    rotateButton.pack()
    breakButton = tk.Button(root,
    text = "break",
    command = cube.collapses)
    breakButton.pack()
    moveCameraButton = tk.Button(root,
    text = "move camera",
    command = movecamera)
    moveCameraButton.pack()
    root.mainloop()