from graphics import *
import sys 
width = 1200
height = 1200
def hCurve(n,x,y,win):
    if n > 0:
        x,y = aCurve(n-1,x,y,win)
        x,y = goSouth(x,y,win)
        x,y = hCurve(n-1,x,y,win)
        x,y = goEast(x,y,win)
        x,y = hCurve(n-1,x,y,win)
        x,y = goNorth(x,y,win)
        x,y = bCurve(n-1,x,y,win)
    return x,y
def aCurve(n,x,y,win):
    if n > 0:
        x,y = hCurve(n-1,x,y,win)
        x,y = goEast(x,y,win)
        x,y = aCurve(n-1,x,y,win)
        x,y = goSouth(x,y,win)
        x,y = aCurve(n-1,x,y,win)
        x,y = goWest(x,y,win)
        x,y = cCurve(n-1,x,y,win)
    return x,y
def bCurve(n,x,y,win):
    if n > 0:
        x,y = cCurve(n-1,x,y,win)
        x,y = goWest(x,y,win)
        x,y = bCurve(n-1,x,y,win)
        x,y = goNorth(x,y,win)
        x,y = bCurve(n-1,x,y,win)
        x,y = goEast(x,y,win)
        x,y = hCurve(n-1,x,y,win)
    return x,y
def cCurve(n,x,y,win):
    if n > 0:
        x,y = bCurve(n-1,x,y,win)
        x,y = goNorth(x,y,win)
        x,y = cCurve(n-1,x,y,win)
        x,y = goWest(x,y,win)
        x,y = cCurve(n-1,x,y,win)
        x,y = goSouth(x,y,win)
        x,y = aCurve(n-1,x,y,win)
    return x,y
def goEast(x,y,win):
    line = Line(Point(x,y), Point(x+32,y))
    line.draw(win)
    return x+32, y
def goWest(x,y,win):
    line = Line(Point(x,y), Point(x-32,y))
    line.draw(win)
    return x-32,y
def goNorth(x,y,win):
    line = Line(Point(x,y), Point(x,y - 32))
    line.draw(win)
    return x,y-32
def goSouth(x,y,win):
    line = Line(Point(x,y), Point(x,y + 32))
    line.draw(win)
    return x,y+32
    
def main():
    #Set  up the canvas
    win = GraphWin("Hilbert Curves",width, height)
    x = int(sys.argv[1])
    hCurve(x,30,30,win) 
    win.getMouse()
    win.close()
main()