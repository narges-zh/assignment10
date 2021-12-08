from os import stat
import random
import arcade
import time
from arcade.key import DOWN, O


SCREEN_WIDTH=500
SCREEN_HEIGHT=5


class Snake(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)

        
        self.width=16
        self.height=16
        self.color=arcade.color.GREEN
        self.body_size=[]
        self.center_x=SCREEN_WIDTH//2
        self.center_y=SCREEN_HEIGHT//2
        self.speed=4
        self.change_x=0
        self.change_y=0
        self.score=0
        self.body_size.append([self.center_x,self.center_y])

    
    def eat(self,n):
        if n=='food':
            self.score+=1
        elif n=='pear':
            self.score+=2
        elif n=='chocolate':
            self.score-=1

       

    def draw(self):
        for i in range(len(self.body_size)):
            if i % 3==0:
                arcade.draw_circle_filled(self.body_size[i][0],self.body_size[i][1],self.color)
            elif i % 3==1:
                arcade.draw_circle_filled(self.body_size[i][0],self.body_size[i][1],arcade.color.SAND)
            else:
                arcade.draw_circle_filled(self.body_size[i][0],self.body_size[i][1],arcade.color.RED)

    def move(self):
        for i in range(len(self.body_size)-1,0,-1):
            self.body_size[i][0]=self.body_size[i-1][0]
            self.body_size[i][1]=self.body_size[i-1][1]
        self.center_x+=self.speed * self.change_x
        self.center_y+=self.speed * self.change_y
        if self.body_size:
            self.body_size[0][0]+=self.speed * self.change_x
            self.body_size[0][1]+=self.speed * self.change_y 


class Pear(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self) 
        self.img='img/pear.jpg'
        self.pear=arcade.Sprite(self.img,0.09)
        self.pear.center_x=random.randint(0,SCREEN_WIDTH) 
        self.pear.center_y=random.randint(0,SCREEN_HEIGHT)

    def draw(self):
        self.pear.draw()

class Chocolate(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self) 
        self.img='img/choco.jpg'
        self.choco=arcade.Sprite(self.img,0.09)
        self.choco.center_x=random.randint(0,SCREEN_WIDTH) 
        self.choco.center_y=random.randint(0,SCREEN_HEIGHT)

    def draw(self):
        self.choco.draw()




class Food(arcade.Sprite):
     def __init__(self):
        arcade.Sprite.__init__(self) 
        self.img='img/food.jpg'
        self.food=arcade.Sprite(self.img,0.09)
        self.food.center_x=random.randint(0,SCREEN_WIDTH) 
        self.food.center_y=random.randint(0,SCREEN_HEIGHT)

     def draw(self):
        self.food.draw()

    


class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,500,500,'snake game')
        arcade.set_background_color(arcade.color.SAND)
        self.snake=Snake(500,500)
        self.food=Food(500,500)
        self.pear=Pear(500,500)
        self.chocolate=Chocolate(500,500)


    def on_draw(self):#har chizi k mikham to safhe ja bshe
        arcade.start_render()
        if self.snake.center_x<=0 or self.snake.center_x>=500 \
          or self.snake.center_y<=0 or self.snake.center_y>=500 \
              or self.snake.score<0:

          arcade.draw_text('Game Over',start_x=120,stat_y=250,color=arcade.color.GOLD,font_size=50)
          arcade.exit()

        else:
          self.snake.draw()
          self.food.draw()
          self.pear.draw()
          self.chocolate.draw()

          arcade.draw_text('Score:%i'%self.snake.score,stat_x=10,stat_y=10,color=arcade.color.RED,font_size=20)

    def on_update(self):#etefaghat bazi ra moshahede mikonim
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.food.food):
            self.snake.eat('food')
            self.snake.body_size.append([self.snake.body_size[len(self.snake.body_size)-1][0],
            self.snake.body_size[len(self.snake.body_size)-1][1]])
            self.food=Food(500,500)

        elif arcade.check_for_collision(self.snake,self.pear.pear):
            self.snake.eat('pear')
            self.snake.body_size.append([self.snake.body_size[len(self.snake.body_size)-1][0],
            self.snake.body_size[len(self.snake.body_size)-1][1]])
            self.pear=Pear(500,500)

        elif arcade.check_for_collision(self.snake,self.chocolate.choco):
            self.snake.eat('chocolate')
            self.chocolate=Chocolate(500,500)

    def on_key_release(self, key: int, modifiers: int):

       if key==arcade.key.LEFT:
         self.snake.center_x-=self.snake.speed
       elif key==arcade.key.RIGHT:
         self.snake.center_x+=self.snake.speed
       elif key==arcade.key.UP:
         self.snake.center_y+=self.snake.speed
       elif key==arcade.key.DOWN:
         self.snake.center_y-=self.snake.speed

my_game=Game()
arcade.run()
        