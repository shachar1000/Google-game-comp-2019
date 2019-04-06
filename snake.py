
#########################################################################################################
#בסד



import os
import time
import sys
from random import randint
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
import nn





def demo(screen):
    
    
    
    interval = 500/1000 #ms
    width = 50
    height = 20
    directions = {
    "right" : {"x" : 1, "y" : 0},
    "left" : {"x" : -1, "y" : 0},
    "up" : {"x" : 0, "y" : -1},
    "down" : {"x" : 0, "y" : 1}
    }
    COLOUR_GREEN = 2

    class food():
        def __init__(self, snake):
            self.x = randint(0, width-1)
            self.y = randint(0, height-1)

            
    class snake:
        def __init__(self, size, color, startX, startY):
            self.body = [{"x":i+startX, "y":startY} for i in range(size)]
            self.direction = directions["right"]
            self.color = color
            self.score = 0
            self.createFood()
            #self.update()
            
        def move(self):
            ate = False
            head = self.body[len(self.body)-1]
            if (self.food.x == head["x"] and self.food.y == head["y"]):
                ate = True
                self.createFood()
            self.body.insert(len(self.body), {
            "x": head["x"]  + self.direction["x"]   ,
            "y": head["y"]  + self.direction["y"]   })
            if not ate:
                self.body.pop(0)
                
        def whereFood(self):
            head = self.body[len(self.body)-1]
            foodDir = {"left": False, "right": False, "up": False}
            if self.food.x - head["x"] < 0:
                foodDir["left"] = True
            elif (self.food.x - head["x"] is not 0):
                foodDir["right"] = True
            if self.food.y - head["y"] < 0:
                foodDir["up"] = True
            
            if self.direction is directions["down"]:
                for key, value in foodDir.items():
                    foodDir[key] = not foodDir[key] if (self.food.x is not head["x"]) else False if key is not "up" else not foodDir[key] #not false = true, not true = false
                
            if self.direction is directions["right"]:
                pass
            
            if self.direction is directions["left"]:
                pass
                        
            screen.print_at("left: "+str(foodDir["left"]), 0, 20)
            screen.print_at("right: "+str(foodDir["right"]), 0, 21)
            screen.print_at("up: "+str(foodDir["up"]), 0, 22)
            screen.refresh()
            
        def checkCollision(self):
            count = 0
            head = self.body[len(self.body)-1]
            for square in self.body:
                if square["x"] is head["x"] and square["y"] is head["y"]:
                    count = count + 1
            if count is 2:
                return False    
            return (-1 < head["x"] < width) and (-1 < head["y"] < height)    
        def draw(self, first=False, last=False):
            for y in range(height):
                #filtered = [square["x"] for square in self.body if square["y"] == y]
                #row = ["O" if x in filtered else "_" for x in range(width)]
                #screen.print_at("".join(row), 0, y)
                if first:
                    screen.print_at("_"*width, 0, y)
                filtered = [square["x"] for square in self.body if square["y"] == y]
                for x in filtered:
                    screen.print_at("O", x, y, self.color)
            screen.print_at("J", self.food.x, self.food.y, self.color)
            if last:
                screen.refresh()
        def check(self, dir):
            for key in self.direction:
                if directions[dir][key] == self.direction[key]*-1:
                    return False
            return True
        def createFood(self): 
            self.food = food(self) # self = snake
            
    snakes = []
    snakes.append(snake(3, 2, 3, 10))
    #snakes.append(snake(3, 3, 5, 12))
    
    
    def update():
        event = screen.get_event()
        for i in range(len(snakes)):
            if isinstance(event, KeyboardEvent):
                key = event.key_code
                if key == Screen.KEY_UP:
                    snakes[i].direction = directions["up"] if snakes[i].check("up") else snakes[i].direction
                elif key == Screen.KEY_DOWN:
                    snakes[i].direction = directions["down"] if snakes[i].check("down") else snakes[i].direction
                elif key == Screen.KEY_LEFT:
                    snakes[i].direction = directions["left"] if snakes[i].check("left") else snakes[i].direction
                elif key == Screen.KEY_RIGHT:
                    snakes[i].direction = directions["right"] if snakes[i].check("right") else snakes[i].direction
    
            if not (snakes[i].checkCollision()):
                os.execl(sys.executable, sys.executable, *sys.argv)
            snakes[i].move()
            snakes[i].whereFood()
            if len(snakes) is not 1:
                if i is 0:
                    snakes[i].draw(True)
                elif i is len(snakes)-1:
                    snakes[i].draw(False, True)
                else:
                    snakes[i].draw()
            else:
                snakes[i].draw(True, True)
                    
        time.sleep(interval)
        update() 
    update()
    
Screen.wrapper(demo)


################################################################################################################################
