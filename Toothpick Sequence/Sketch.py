from graphics import *
from Toothpick import Toothpick
import sys
width = 600
height = 600
def main():
    #Set  up the canvas
    win = GraphWin("My toothpick", width, height)
    win.setBackground("white")
    win.setCoords(-width/2, -height/2, width/2, height/2)
    #Create list for all of the toothpicks
    toothpicks = []
    #Create first toothpick and add it to list
    toothpick = Toothpick(0, 0, 'horizontal')
    toothpicks.append(toothpick)
    print(f'Iteration #0: #Toothpicks added in this iteration: 1, Total #toothpicks: 1')
    #For lopp of iterations
    for i in range(int(sys.argv[1])):
        toothpicks_added = 0
        new_toothpick = []
        #Create 2 new toothpicks for each toothpick if possible
        for toothpick in toothpicks:
            if not toothpick.alreadyShown:
                #Show toothpick on canvas 
                toothpick.show(win)
            toothpick_A = toothpick.toothpickToAddA(toothpicks)
            toothpick_B = toothpick.toothpickToAddB(toothpicks)
            #Add toothpicks to new list
            if toothpick_A != None:
                new_toothpick.append(toothpick_A)
                toothpicks_added += 1
            if toothpick_B != None:
                new_toothpick.append(toothpick_B)
                toothpicks_added += 1
        #Add the list with new toothpicks to the toothpicks list
        toothpicks = toothpicks + new_toothpick
        #win.getMouse() #in for loop to see each iteration
        print(f'Iteration #{i + 1} #Toothpicks added in this iteration: {toothpicks_added}, Total #toothpicks: {len(toothpicks)}')
    win.getMouse()
    win.close()
main()