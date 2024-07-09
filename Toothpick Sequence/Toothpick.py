from graphics import *
class Toothpick():
    LENGTH = 63
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.alreadyShown = False
    def blockedA(self, other):
        if self.direction == 'horizontal' and other.direction == 'horizontal':
            return other.x + (Toothpick.LENGTH // 2) == self.x - (Toothpick.LENGTH // 2) and other.y == self.y
        elif self.direction == 'horizontal' and other.direction == 'vertical':
            return other.x == self.x - (Toothpick.LENGTH // 2) and other.y == self.y
        elif self.direction == 'vertical' and other.direction == 'horizontal':
            return other.y == self.y - (Toothpick.LENGTH // 2) and other.x == self.x
        else:
            return other.y + (Toothpick.LENGTH // 2) == self.y - (Toothpick.LENGTH // 2) and other.x == self.x
    def blockedB(self, other):
        if self.direction == 'horizontal' and other.direction == 'horizontal':
            return other.x - (Toothpick.LENGTH // 2) == self.x + (Toothpick.LENGTH // 2) and other.y == self.y 
        elif self.direction == 'horizontal' and other.direction == 'vertical':
            return other.x == self.x + (Toothpick.LENGTH // 2) and other.y == self.y
        elif self.direction == 'vertical' and other.direction == 'horizontal':
            return other.y == self.y + (Toothpick.LENGTH // 2) and other.x == self.x
        else:
            return other.y - (Toothpick.LENGTH // 2) == self.y + (Toothpick.LENGTH // 2) and other.x == self.x
    def toothpickToAddA(self, toothpicks):
        for toothpick in toothpicks:
            if self.blockedA(toothpick):
                return None
        if self.direction == 'horizontal':
            return Toothpick(self.x - (Toothpick.LENGTH // 2), self.y, 'vertical')
        if self.direction == 'vertical':
            return Toothpick(self.x, self.y - (Toothpick.LENGTH // 2), 'horizontal')
    def toothpickToAddB(self, toothpicks):
            for toothpick in toothpicks:
                if self.blockedB(toothpick):
                    return None
            if self.direction == 'horizontal':
                return Toothpick(self.x + (Toothpick.LENGTH // 2), self.y, 'vertical')
            if self.direction == 'vertical':
                return Toothpick(self.x, self.y + (Toothpick.LENGTH // 2), 'horizontal')
    def show(self, win):
        if self.direction == "horizontal":
            p1 = Point(self.x - (Toothpick.LENGTH // 2), self.y)
            p2 = Point(self.x + (Toothpick.LENGTH // 2), self.y)
            line = Line(p1, p2)
            line.draw(win)
        else:
            p1 = Point(self.x, self.y - (Toothpick.LENGTH // 2))
            p2 = Point(self.x, self.y + (Toothpick.LENGTH // 2))
            line = Line(p1, p2)
            line.draw(win)
        self.alreadyShown = True