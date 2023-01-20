from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()

root.geometry("1400x800")
root.maxsize(1400, 800)
root.minsize(1400, 800)
movement = 40

class Space(Canvas):
    def __init__(self):
        super().__init__(width = 1400,
                         height = 800,
                         bg = 'black')
        self.pack()
        self.import_imgs()
        self.sspos = [700, 760]
        self.bpos = []
        self.enemypos = []
        self.score = 0
        self.game = True
        self.parscore = 500
        self.time_enemymove = 1000
        self.time_enemygen = 4000
        self.mainscore = 100
        self.bind_all('<Key>', self.onClick)

        self.after(100, self.action)

        self.after(self.time_enemymove, self.moveEmy)

        self.after(self.time_enemygen, self.genEmy)

    def import_imgs(self):
        self.ss = ImageTk.PhotoImage(Image.open('spaceship.png'))
        self.es = ImageTk.PhotoImage(Image.open('enemy.png'))
        self.bullet = ImageTk.PhotoImage(Image.open('bullet.png'))

    def onClick(self, e):
        if e.keysym == 'Right':
            if self.sspos[0] == 1380: return
            self.sspos[0] += movement
        elif e.keysym == 'Left':
            if self.sspos[0] == 20: return
            self.sspos[0] -= movement
        elif e.keysym == 'Up':
            if self.sspos[1] == 40: return
            self.sspos[1] -= movement
        elif e.keysym == 'Down':
            if self.sspos[1] == 760: return
            self.sspos[1] += movement
        elif e.keysym == 'space':
            self.bpos.append([self.sspos[0], self.sspos[1] - 2 * movement, True])
        self.coords(
            self.find_withtag('spaceship'),
            *self.sspos
        )

    def identify(self, e):
        if e[1] > 760:
            self.gameOver()
        return e[2]

    def action(self):
        if self.score > self.parscore and self.time_enemymove > 400:
            self.parscore += 500
            self.time_enemymove -= 100
            self.time_enemygen -= 500
            self.mainscore += 100
        self.delete(ALL)
        root.title(f'Score : {self.score}')
        for i in range(len(self.bpos)):
            if self.bpos[i][1] < 0:
                self.bpos[i][2] = False
            else:
                self.bpos[i][1] -= movement
                self.create_image(self.bpos[i][0], self.bpos[i][1], image = self.bullet)
            for j in range(len(self.enemypos)):
                if (((self.enemypos[j][0] - 40) <= (self.bpos[i][0] - 10) <= (self.enemypos[j][0] + 40)) or ((self.enemypos[j][0] - 40) <= (self.bpos[i][0] + 10) <= (self.enemypos[j][0] + 40))) and (((self.enemypos[j][1] - 40) <= (self.bpos[i][1] - 10) <= (self.enemypos[j][1] + 40)) or ((self.enemypos[j][1] - 40) <= (self.bpos[i][1] + 10) <= (self.enemypos[j][1] + 40))):
                    self.bpos[i][2] = False
                    self.enemypos[j][2] = False
                    self.score += self.mainscore
                    break
        self.enemypos = list(filter(self.identify, self.enemypos))
        for i in self.enemypos:
            self.create_image(*i[:2], image = self.es) 
        self.create_image(*self.sspos, image = self.ss, tag = 'spaceship')
        self.bpos = list(filter(lambda x: x[2], self.bpos))
        if self.game:
            self.after(100, self.action)
        else:
            self.gameOver()

    def gen_enemy(self):
        x, y = randint(1, 34) * 40, 40
        self.enemypos.append([x, y, True])

    def moveEmy(self):
        for i in self.enemypos:
            i[1] += 40
        if self.game:
            self.after(self.time_enemymove, self.moveEmy)
        else:
            self.gameOver()

    def genEmy(self):
        self.gen_enemy()
        if self.game:
            self.after(self.time_enemygen, self.genEmy)
        else:
            self.gameOver()

    def gameOver(self):
        self.game = False
        self.delete(ALL)
        self.create_text(700, 400, text = f'Game Over !! Your Final Score is {self.score}', font = ('algerian', 28, 'bold'), fill = 'red')
    
game = Space()

root.mainloop()