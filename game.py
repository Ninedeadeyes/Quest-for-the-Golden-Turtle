

import turtle
import math
import random
import time
import winsound

wn= turtle.Screen()
wn.bgcolor("black")
wn.title("Quest For The Golden Turtle")
wn.setup(800,800)
wn.tracer(0)


images=[".\\art\\wall.gif",".\\art\\orkleft.gif",".\\art\\ork.gif",".\\art\\orkup.gif",".\\art\\gold.gif",".\\art\\fire.gif",".\\art\\door.gif",".\\art\\orkright.gif",".\\art\\arrowup.gif",
        ".\\art\\arrowdown.gif",".\\art\\arrowright.gif",".\\art\\arrowleft.gif",".\\art\\heroleft.gif",".\\art\\heroright.gif",".\\art\\herodown.gif",".\\art\\heroup.gif"]

for image in images:
    turtle.register_shape(image)


class Info():
    def __init__(self):
        self.gold = 0
        self.exp =0
        self.lives=3
        self.pen = turtle.Turtle()

        
    def draw_border(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-324, 324)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(645)
            self.pen.rt(90)
            self.pen.fd(665)
            self.pen.rt(90)
            
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
        
    def show_gold(self):
        self.pen.undo()
        msg = "Gold: %s"  %(game.gold)
        self.pen.penup()
        self.pen.goto(-324, 334)
        self.pen.write(msg, font=("Arial", 16, "normal"))


    def show_rules(self):
        msg = ("Controls: W,A,S,D Arrow Keys")
        self.pen.penup()
        self.pen.goto(-324, -380)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        self.pen.pendown()
        self.pen.penup()
        self.pen.ht()
     

    def win(self):
        msg= (""" 
   You found the Golden Turtle !! You win !!
                      Click (x) to exit
 
               """)
        self.pen.penup()
        self.pen.goto(-250,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def dead(self):
        msg= (""" 
                        (Game Over)    
                      Click (x) to exit
 
               """)
        self.pen.penup()
        self.pen.goto(-250,304)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        
    def show_lives(self):
        self.pen.undo()
        msg = " Credit:%s" %(life.lives)
        self.pen.penup()
        self.pen.ht()
        self.pen.goto(250,-380)
        self.pen.color("white")         
        self.pen.write(msg, font=("Arial", 16, "normal"))
    

    def show_exp(self):
        self.pen.undo()
        self.pen.penup()
        self.pen.ht()
        self.pen.goto(250,334)
        self.pen.color("white")
        msg = " XP:%s" %(xp.exp)        
        self.pen.write(msg, font=("Arial", 16, "normal"))
    
    

    def lose(self):     #this is just experimenting , not in game
        wn.clear()
        wn.bgcolor("blue")
        self.goto(0, 0)
        self.color("white")
        self.write("Sorry, you lose."'\n'  "Your xp: {} points".format(self.exp), False, align="center",
                         font=("Arial", 16, "normal"))

        

class Missile(turtle.Turtle):
    def __init__(self,startx, starty):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\arrowright.gif")
        self.speed = 4
        self.fd(10)
        self.penup()
        self.color("yellow")
        self.status = "ready"
        self.goto(-1000, 1000)

    def is_collision(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 20:
            return True
        else:
            return False

    def is_far(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance >100:
            return True
        else:
            return False
            

    def fire(self):
         if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            if lives != 3:
                winsound.PlaySound(".\\sound\\arrow.wav", winsound.SND_ASYNC)


           
            
    def move(self):
    
        if self.status == "ready":
            self.goto(-2456, 3422)
            
        
        if self.status == "firing":
            self.fd(self.speed) 
            
        #Border check


        if missile.is_far(player):
            self.setheading(player.heading())
            self.status = "ready"               
        
          
        if self.xcor() < -350 or self.xcor() > 300 or \
            self.ycor()< -350 or self.ycor()> 300:
            self.setheading(player.heading())
            self.status = "ready"

        if (self.xcor(), self.ycor()) in walls:           
            self.setheading(player.heading())
            self.status = "ready"
            



class Crown(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold= 100
        self.goto(x,y)

    def destroy(self):
        self.goto(1998,1998)
        self.hideturtle()
      

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.fd(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\heroright.gif")
        self.penup()
        self.speed()
        self.fd(0)
        self.right=1
        self.left=0
        self.up=0
        self.down=0


    def headright(self):

        if self.right==1:
            pass

        if self.down==1:
            self.rt(270)
            self.down=0
            self.right=1         
            
        if self.left==1:
            self.rt(180)
            self.left=0
            self.right=1

        if self.up==1:
            self.rt(90)
            self.up=0
            self.right=1

        self.shape(".\\art\\heroright.gif")
        missile.shape(".\\art\\arrowright.gif")  #This is needed because it change the character directon shape to the direction of the fire. 
        missile.fire()


    def headdown(self):

        if self.down==1:
            pass

        if self.left==1:
            
            self.rt(270)
            self.left=0
            self.down=1


        if self.up==1:
            
            self.rt(180)
            self.up=0
            self.down=1
    
        if self.right==1:
            
            self.rt(90)
            self.right=0
            self.down=1

        self.shape(".\\art\\herodown.gif")
        missile.shape(".\\art\\arrowdown.gif")
        missile.fire()



    def headleft(self):

        if self.left==1:
            pass

        if self.up==1:
            
            self.rt(270)
            self.up=0
            self.left=1

        if self.right==1:
            
            self.rt(180)
            self.right=0
            self.left=1

        if self.down==1:
            
            self.rt(90)
            self.down=0
            self.left=1

        self.shape(".\\art\\heroleft.gif")
        missile.shape(".\\art\\arrowleft.gif")
        missile.fire()
            
    def headup(self):
          
        if self.up==1:
            pass

        if self.right==1:
            
            self.rt(270)
            self.right=0
            self.up=1

        if self.down==1:
            
            self.rt(180)
            self.down=0
            self.up=1

        if self.left==1:
            
            self.rt(90)
            self.left=0
            self.up=1
            
        self.shape(".\\art\\heroup.gif")
        missile.shape(".\\art\\arrowup.gif")
        missile.fire()
            

         

    def go_up(self):

        move_to_x = self.xcor()
        move_to_y = self.ycor()+24

        self.shape(".\\art\\heroup.gif")

        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
      
        
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        self.shape(".\\art\\herodown.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
        
        
    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.shape(".\\art\\heroleft.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        
        
    def go_right(self):
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()
        self.shape(".\\art\\heroright.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
        

    def is_collision(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 10:
            return True
        else:
            return False


    def destroy(self):
        self.goto(500,500)
        self.hideturtle()


        
        
class Coin(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\gold.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold= 100
        self.goto(x,y)

    def destroy(self):
        self.goto(1998,1998)
        self.hideturtle()

class Door(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape((".\\art\\door.gif"))
        self.color("brown")
        self.penup()
        self.speed(0)
        self.gold= 100
        self.goto(x,y)

    def destroy(self):
        self.goto(1999,1999)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\orkleft.gif")
        self.color("red")
        self.penup()
        self.exp= 5
        self.speed(0)
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])


    def is_close(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 100:
            return True
        else:
            return False
                


    def move(self):
        if self.direction =="up":
            dx= 0
            dy= 24
            self.shape(".\\art\\orkup.gif")
            
        elif self.direction =="down":
            dx= 0
            dy= -24
            self.shape(".\\art\\ork.gif")
          
        elif self.direction =="left":
            dx= -24
            dy= 0
            self.shape(".\\art\\orkleft.gif")

        elif self.direction =="right":
            dx= 24
            dy= 0
            self.shape(".\\art\\orkright.gif")
 
        else:
            dx = 0
            dy = 0


        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"

            elif player.xcor()>self.xcor():
                self.direction="right"

            elif player.ycor()<self.ycor():
                self.direction="down"

            elif player.ycor()>self.ycor():
                self.direction="up"
                                                                        
            
        # Calculate the spot to move to 
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move,t=random.randint(100,300))





  
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


lives=0

crowns=[]
enemies =[]   
coins =[]
doors =[]

levels = [""]

level_1 =[

"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XX                E  X",
"X  XX  XXXXXXXXXXXX     X",
"X      XXXXXXXXXXXX     X",    
"X     CXXCCE        XXXXX",     
"XXXXXXXXXXXXXXXXXX  XXXXX",
"XXXXCCCXXXXXXXXXXX  XXXXX",
"XXXXX        E XXX  XXXXX",
"XX        XXX  XXX  XXXXX",
"XX  X     XXX  XXX  XXXXX",
"XX  X  E  XXX  XXX  XXXXX",
"X   XXXX  XXX           X",
"XCCCXXXX  XXXXXXXXXXXXX X",
"XXXXXXXX  XXXXXXXXXXXXX X",
"XXX        EXX   CCCXXXCX",
"XXX         XX   CCCXXXCX",
"XXX  XXXXXXXXXXXX   XXXCX",
"XXX  XX  CCXXXXXX   XXXXX",
"XXX  XX  CCXXXXXX   XXXXX",
"XXX  XX    XXXXXX    XXXX",
"XC   XXE XXXXXXXX E  XXXX",
"XXXX XX  XXXXXXXX XXXXXXX",
"XCC         XX    XXXXXXX",
"XXXD            E XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]


level_2 =[


"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                      X",
"X    XXXXXXXXXXXX       X",
"X               XE      X",
"X       E  XXX  X       X",
"X          XXX  X   CCCCX",
"XXXXXXXXXXXXXX  XXXXXXXXX",
"XCCXXXXXXXXXXX          X",
"XCCCX                   X",
"X   X  E    XXXXXX      X",
"X           XXXXXX  CCCCX",
"X   XXXXXXXXXXXXXXXXXXXXX",
"X     XXCCCCXXXXXX  E   X",
"X     XXCCCCCCC         X",
"X     XXXXXXXXXXXX   E  X",
"X     XXE        X      X",
"X     XX         X      X",
"X   E XX    XX E X      X",
"X     XX    XX   X    C X",
"X     XX   EXX   X    C X",
"X     XX    XX        C X",
"X           XX   X   CC X",
"X      E    XX E XXXXXXXX",
"X           XX         DX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]


level_3 =[


"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XC                      X",
"XC E    XXX XXXX XX     X",
"XC   E  X         X     X",
"XC      X         X    DX",
"XC    E X         XXXXXXX",
"XXXXXXXXX               X",
"X  E   E    E           X",
"X      CCCCCCC          X",
"X  E  XXXXXXXXX         X",
"X     XXXXXXXXX     E   X",
"X    CXXXXXXXXXC        X",
"X  E CXXX P XXXC        X",
"X    CXXX   XXXC        X",
"X    CXXC   CXXC        X",
"X    CXX     XXC    E   X",
"X     XX     XX         X",
"X  E  XXXX XXXX         X",
"X        X X      E     X",
"X        X X            X",
"X                       X",
"X          E            X",
"X           E           X",
"X  E                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]

level_4 =[

"XXXXXXXXXXXXXXXXXXXXXXXX",
"XP                  E  X",
"XXXXXX                 X",
"X                      X",
"X      E         E     X",
"X                      X",
"XE                   E X",
"XXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXX",
"X                      X",
"X                      X",
"X     CCCCCCCCCCC      X",
"X     CCCCCCCCCCC      X",
"X     CCCCCCCCCCC      X",
"X     CCCCCCCCCCC      X",
"X                      X",
"X           D          X",
"XXXXXXXXXXXXXXXXXXXXXXXX",


    ]


level_5 =[

"XXXXXXXXXXXXXXXXXXXXXXXX",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X                      X",
"X           M          X",
"X                      X",
"X                      X",
"X     P                X",
"X                      X",
"X                      X",
"XXXXXXXXXXXXXXXXXXXXXXXX",
]

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)

#row are y ( up/down) column are x (left and right )
# 

def setup_maze(level):
    for y in range (len(level)): #tell how many rows there is 
        for x in range(len(level[y])): # acquire every x of the y row
            #Get the character at each x,y coordinate
            #NOTE the order of Y AND X in the next line
            character = level [y][x]
            #Calculate the screen x,y coordinates.  Furtherest left upper corner is (0,0)
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            #check if it is an x  represent a wall
            if character == "X":   
                pen.goto(screen_x, screen_y)
                pen.shape(".\\art\\wall.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
                
            if character == "P":   # p= player 
                player.goto(screen_x, screen_y)

            if  character == "C":
                coins.append(Coin(screen_x, screen_y))
                
            if character =="E":
                enemies.append(Enemy(screen_x, screen_y))

            if character =="D":
                doors.append(Door(screen_x, screen_y))

            if character =="M":
                crowns.append(Crown(screen_x, screen_y))
                
              
              
pen=Pen()
player= Player()
missile = Missile(0, 0)
walls=[]

setup_maze(levels[1])
maze=("level1")

life=Info()
xp=Info()
game=Info()
game.draw_border()
game.show_rules()
game.show_gold()
xp.show_exp()
life.show_lives()


#keyboard binding

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.headright, "d")
turtle.onkey(player.headleft, "a")
turtle.onkey(player.headdown,"s")
turtle.onkey(player.headup,"w")
turtle.onkey(player.headright, "D")
turtle.onkey(player.headleft, "A")
turtle.onkey(player.headdown,"S")
turtle.onkey(player.headup,"W")

for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)


while True:

    
    missile.move()


    for crown in crowns:
        
        if player.is_collision(crown):

            player.destroy()
            crown.destroy()
            crowns.remove(crown)
            lives=3
            game.win()
            winsound.PlaySound(".\\sound\\victory.wav",0)
            
                 

    for enemy in enemies:
        if missile.is_collision(enemy):
            Enemy.destroy(enemy)
            missile.status = "ready"
            xp.exp += enemy.exp
            xp.show_exp()
            winsound.PlaySound(".\\sound\\orkdeath.wav", winsound.SND_ASYNC)
            
    for coin in coins:
        if player.is_collision(coin):
            game.gold += coin.gold
            game.show_gold()
            #print("Player Gold: {}".format (game.gold))
            coin.destroy()
            coins.remove(coin)
            winsound.PlaySound(".\\sound\\coin.wav", winsound.SND_ASYNC)

    for enemy in enemies:
        if player.is_collision(enemy):
            lives+=1
            life.lives-=1
            winsound.PlaySound(".\\sound\\death.wav", winsound.SND_ASYNC)
            time.sleep(1)
            print("Player dies ")
            walls.clear()
            pen.clear()       
            for enemy in enemies:
                Enemy.destroy(enemy)
            for coin in coins:
                Coin.destroy(coin)
            for door in doors:
                Door.destroy(door)

            if lives==3:
                game.dead()
                #xp.lose()    
                player.destroy()
                setup_maze(levels[1])
                life.show_lives()
                break
            
            
            game.gold=0
            xp.exp=0
            xp.show_exp()
            life.show_lives()
            game.show_gold()
            setup_maze(levels[1])
            maze=("level1")
            for enemy in enemies:
                turtle.ontimer(enemy.move,t=250)  

              
            

    for door in doors:
        if player.is_collision(door):
            walls.clear()
            pen.clear()
            for enemy in enemies:
                Enemy.destroy(enemy)
            for coin in coins:
                Coin.destroy(coin)
            for door in doors:
                Door.destroy(door)
            winsound.PlaySound(".\\sound\\unlock.wav", winsound.SND_ASYNC)
    
            
            if maze==("level1"):
            
                setup_maze(levels[2])
                maze=("level2")
                
            elif maze ==("level2"):
                setup_maze(levels[3])
                maze=("level3")
                
            elif maze==("level3"):
                setup_maze(levels[4])
                maze=("level4")


            elif maze==("level4"):
                setup_maze(levels[5])
        
                   
            else:
                pass

            
             
            for enemy in enemies:
                turtle.ontimer(enemy.move,t=250)



    wn.update()

