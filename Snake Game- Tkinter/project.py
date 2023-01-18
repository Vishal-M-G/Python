from tkinter import *
from PIL import Image, ImageTk
from random import randint

base = Tk()

base.geometry("800x600")
base.title("Snake Game")
base.resizable(False, False)
movement = 20

class Board(Canvas):
    def __init__(self):
        super().__init__(width = 800,
                         height = 600,
                         bg = 'black')
        self.pack()
        self.bind_all("<Key>", self.onClick)
        self.score = 0
        self.snakepos = [[40, 60], [40 + movement, 60], [40 + movement * 2, 60]]
        self.direction = 'Right'

        self.image_loader()
        self.setFood()
        self.create_elements()

        self.after(100, self.action)

    def image_loader(self):
        self.snake = ImageTk.PhotoImage(Image.open('snake.png'))
        self.food = ImageTk.PhotoImage(Image.open('apple.png'))

    def create_elements(self):
        self.create_text(70, 20,
                         text = f"Score : {self.score}",
                         fill = 'white',
                         font = ('algerian', 20, 'bold'))

        self.create_rectangle(20, 40, 780, 580, outline = 'white', width = 3)

        for i, j in self.snakepos:
            self.create_image(i, j, image = self.snake)

        self.create_image(self.foodpos[0], self.foodpos[1], image = self.food)

    def action(self):
        self.delete(ALL)
        self.snakepos.pop(0)
        self.snakepos.append(self.snakepos[-1][:])
        if self.direction == 'Right':
            self.snakepos[-1][0] += movement
        elif self.direction == 'Left':
            self.snakepos[-1][0] -= movement
        elif self.direction == 'Up':
            self.snakepos[-1][1] -= movement
        elif self.direction == 'Down':
            self.snakepos[-1][1] += movement
        a, b = self.snakepos[-1]
        if a == self.foodpos[0] and b == self.foodpos[1]:
            self.setFood()
            self.score += 100
            self.snakepos.insert(0, self.snakepos[0][:])
        if a <= 20:
            self.snakepos[-1][0] = 760
        elif a >= 780:
            self.snakepos[-1][0] = 40
        elif b <= 40:
            self.snakepos[-1][1] = 560
        elif b >= 580:
            self.snakepos[-1][1] = 60
        self.create_elements()
        if self.ateSelf():
            self.after(1000, self.finishGame())
        else:
            self.after(100, self.action)

    def ateSelf(self):
        a, b = self.snakepos[-1]
        for i, j in self.snakepos[:-1]:
            if a == i and b == j:
                return True
        return False
    
    def finishGame(self):
        self.delete(ALL)
        self.create_text(400, 300, text = f"Game Over\nYour score is {self.score}", fill = 'white', font=('algerian', 20, 'bold'))

    def onClick(self, e):
        if e.keysym == self.direction: return
        if e.keysym == 'Up' and self.direction != 'Down' or e.keysym == 'Down' and self.direction != 'Up':
            self.direction = e.keysym
        elif e.keysym == 'Left' and self.direction != 'Right' or e.keysym == 'Right' and self.direction != 'Left':
            self.direction = e.keysym

    def setFood(self):
        x, y = movement + randint(1, 37) * movement, movement + randint(2, 27) * movement
        self.foodpos = (x, y)        
        
game = Board()

base.mainloop()


